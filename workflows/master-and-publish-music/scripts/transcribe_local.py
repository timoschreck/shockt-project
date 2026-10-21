"""Create an unapproved, timestamped song transcription using local faster-whisper.

Requires faster-whisper, numpy and FFmpeg. Audio remains local; model files may download.
The output is evidence for review, not an approved Spotify/Musixmatch submission.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--ffmpeg', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--language', default=None, help='For example de or en; omit to detect')
    parser.add_argument('--model', default='small')
    parser.add_argument('--model-dir', type=Path, required=True)
    parser.add_argument('--cpu-threads', type=int, default=8)
    parser.add_argument('--clip', default='0', help='Optional full-audio second ranges, for example 290,310')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', args.name):
        parser.error('--name must be an ASCII stem without path components')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / (args.name + '.asr-draft.json')
    text_path = args.output_dir / (args.name + '.asr-draft.txt')
    if json_path.exists() or text_path.exists():
        parser.error('Output already exists; choose a new name or output directory')
    import numpy as np
    from faster_whisper import WhisperModel
    with args.input.open('rb') as handle:
        digest = hashlib.file_digest(handle, 'sha256').hexdigest()
    decoded = subprocess.run([str(args.ffmpeg), '-hide_banner', '-loglevel', 'error', '-nostdin',
        '-i', str(args.input), '-map', '0:a:0', '-ar', '16000', '-ac', '1',
        '-c:a', 'pcm_f32le', '-f', 'f32le', '-'], capture_output=True, check=True)
    audio = np.frombuffer(decoded.stdout, dtype='<f4').copy()
    model = WhisperModel(args.model, device='cpu', compute_type='int8', cpu_threads=args.cpu_threads,
                         download_root=str(args.model_dir))
    segments, info = model.transcribe(audio, language=args.language, beam_size=5,
        word_timestamps=True, vad_filter=False, condition_on_previous_text=False,
        temperature=0, clip_timestamps=args.clip)
    rows = []
    for segment in segments:
        row = {'start': segment.start, 'end': segment.end, 'text': segment.text.strip(),
            'avg_logprob': segment.avg_logprob, 'no_speech_probability': segment.no_speech_prob,
            'words': [{'start': word.start, 'end': word.end, 'word': word.word.strip(),
                       'probability': word.probability} for word in (segment.words or [])]}
        rows.append(row)
        print(f'{row["start"]:.2f}-{row["end"]:.2f}: {row["text"]}', flush=True)
    with args.input.open('rb') as handle:
        if hashlib.file_digest(handle, 'sha256').hexdigest() != digest:
            raise RuntimeError('Source changed while transcribing')
    data = {'status': 'unapproved_asr_draft', 'model': args.model, 'language': info.language,
        'source_filename': args.input.name, 'source_sha256': digest,
        'duration_seconds': len(audio) / 16000, 'clip': args.clip,
        'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'segments': rows,
        'listening_review': 'not performed', 'submitted_to_provider': False}
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text_path.write_text('\n'.join(row['text'] for row in rows) + '\n', encoding='utf-8')
    print(f'Saved unapproved draft: {json_path}', flush=True)


if __name__ == '__main__':
    main()
