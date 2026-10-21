"""Conservative technical mastering helper for PCM WAV; Python stdlib + FFmpeg.

This helper performs no subjective listening assessment. Choose parameters per song.
"""
import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import wave


def file_hash(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def wav_info(path):
    with wave.open(str(path), 'rb') as handle:
        frames, rate = handle.getnframes(), handle.getframerate()
        return {'frames': frames, 'sample_rate': rate, 'channels': handle.getnchannels(),
                'bits': handle.getsampwidth() * 8, 'duration_seconds': frames / rate}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ffmpeg', required=True, type=Path)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--name', required=True, help='Unique filename stem, for example artist_title_Master_v1')
    parser.add_argument('--artist', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--target-lufs', type=float, default=-14)
    parser.add_argument('--true-peak', type=float, default=-1)
    parser.add_argument('--highpass-hz', type=float, default=0, help='0 disables filtering')
    parser.add_argument('--fade-in-ms', type=float, default=0)
    parser.add_argument('--fade-out-ms', type=float, default=0)
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', args.name):
        parser.error('--name must be an ASCII filename stem without path components')
    if not (-70 <= args.target_lufs <= -5 and -9 <= args.true_peak <= 0):
        parser.error('Targets outside FFmpeg loudnorm range')
    if not all(math.isfinite(x) and x >= 0 for x in [args.highpass_hz, args.fade_in_ms, args.fade_out_ms]):
        parser.error('Cleanup parameters must be finite and nonnegative')
    source = args.input.resolve()
    info = wav_info(source)
    if info['channels'] != 2:
        parser.error('Helper is for stereo PCM WAV; review mono/multichannel sources separately')
    if args.highpass_hz >= info['sample_rate'] / 2:
        parser.error('Highpass must be below Nyquist')
    if (args.fade_in_ms + args.fade_out_ms) / 1000 >= info['duration_seconds']:
        parser.error('Fades must not overlap')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    wav = args.output_dir / (args.name + '.wav')
    flac = args.output_dir / (args.name + '.flac')
    report_path = args.output_dir / (args.name + '.mastering.json')
    if any(p.exists() for p in [wav, flac, report_path]):
        parser.error('Output already exists; choose a new version or another directory')
    source_hash = file_hash(source)

    def run(options):
        result = subprocess.run([str(args.ffmpeg), '-hide_banner', '-nostats', '-nostdin', *options],
                                capture_output=True, encoding='utf-8', errors='replace')
        if result.returncode:
            raise RuntimeError(result.stderr)
        return result

    def stats(stderr):
        match = re.search(r'\{\s*"input_i".*?\}', stderr, re.S)
        if not match:
            raise RuntimeError('No loudness statistics returned')
        value = json.loads(match.group())
        if not all(math.isfinite(float(value[k])) for k in ['input_i', 'input_tp', 'input_lra', 'input_thresh', 'target_offset']):
            raise RuntimeError('Non-finite loudness: inspect silence or unsupported material')
        return value

    base = f'loudnorm=I={args.target_lufs}:TP={args.true_peak}:LRA=11'

    def measure(path, prefix=''):
        return stats(run(['-i', str(path), '-map', '0:a:0', '-af', prefix + base + ':print_format=json', '-f', 'null', '-']).stderr)

    cleanup = []
    if args.highpass_hz:
        cleanup.append(f'highpass=f={args.highpass_hz}:p=2')
    if args.fade_in_ms:
        cleanup.append(f'afade=t=in:st=0:d={args.fade_in_ms / 1000}')
    if args.fade_out_ms:
        cleanup.append(f'afade=t=out:st={info["duration_seconds"]-args.fade_out_ms / 1000:.9f}:d={args.fade_out_ms / 1000}')
    prefix = ','.join(cleanup) + ',' if cleanup else ''
    original = measure(source)
    measured = measure(source, prefix) if cleanup else original
    gain = args.target_lufs - float(measured['input_i'])
    if float(measured['input_tp']) + gain > args.true_peak - .05:
        raise RuntimeError('Insufficient peak headroom for linear normalization. Review target or limiting explicitly.')
    norm = (base + ':linear=true:'
            f'measured_I={measured["input_i"]}:measured_TP={measured["input_tp"]}:'
            f'measured_LRA={measured["input_lra"]}:measured_thresh={measured["input_thresh"]}:'
            f'offset={measured["target_offset"]}:print_format=json')
    render = stats(run(['-n', '-i', str(source), '-map', '0:a:0', '-map_metadata', '-1', '-af', prefix + norm,
                        '-ar', str(info['sample_rate']), '-ac', '2', '-c:a', 'pcm_s24le',
                        '-metadata', 'artist=' + args.artist, '-metadata', 'title=' + args.title, str(wav)]).stderr)
    if render['normalization_type'] != 'linear':
        raise RuntimeError('Unexpected dynamic normalization; do not publish this output')
    run(['-n', '-i', str(wav), '-map', '0:a:0', '-c:a', 'flac', '-compression_level', '8',
         '-sample_fmt', 's32', '-bits_per_raw_sample', '24', str(flac)])
    final = measure(wav)
    final_info = wav_info(wav)
    for key in ['frames', 'sample_rate', 'channels']:
        if final_info[key] != info[key]:
            raise RuntimeError('Unexpected change to ' + key)
    if abs(float(final['input_i']) - args.target_lufs) > .15 or float(final['input_tp']) > args.true_peak:
        raise RuntimeError('Final loudness/true peak check failed')

    def pcm_hash(path):
        return run(['-i', str(path), '-map', '0:a:0', '-c:a', 'pcm_s24le', '-f', 'hash', '-hash', 'sha256', '-']).stdout.strip()

    pcm_wav, pcm_flac = pcm_hash(wav), pcm_hash(flac)
    if pcm_wav != pcm_flac:
        raise RuntimeError('WAV and FLAC PCM mismatch')
    if file_hash(source) != source_hash:
        raise RuntimeError('Source hash changed')
    report = {'artist': args.artist, 'title': args.title,
              'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'source': {**info, 'filename': source.name, 'sha256': source_hash, 'loudness': original},
              'processing': {'cleanup': cleanup, 'normalization': norm, 'type': render['normalization_type']},
              'final': {**final_info, 'loudness': final, 'wav_sha256': file_hash(wav),
                        'flac_sha256': file_hash(flac), 'decoded_pcm_sha256': pcm_wav},
              'verification': {'source_unchanged': True, 'sample_format_and_duration_pass': True,
                               'loudness_and_true_peak_pass': True, 'flac_equals_wav_pcm': True},
              'listening_review': 'not performed by this script',
              'note': 'Technical master. 24-bit output does not recover missing source information.',
              'tool_version': run(['-version']).stdout.splitlines()[0]}
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'wav': str(wav), 'flac': str(flac), 'report': str(report_path),
                      'verification': report['verification']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
