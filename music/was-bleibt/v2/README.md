# Was bleibt? – Schluss v2

**Technisch geprüfte Hörfassung; Künstlerfreigabe und Liedtextfreigabe offen.**

Für die abgebrochene Schluss-Passage wurde im autorisierten MakeBestMusic-Projekt einmal eine Fortsetzung ab **05:02** erzeugt. Der Dienst lieferte zwei Varianten. Die etwa 35 Sekunden lange Variante wurde zu einer Gesamtfassung zusammengefügt. Die [native Dienstfassung](https://makebestmusic.com/app/shared-music/7bfdb15c-2695-433e-8164-5393cc81ab86) ist separat vom hier abgelegten lokalen Master zu betrachten.

## Lokaler Schnitt und Mastering

Die ursprüngliche bereitgestellte WAV bleibt die Quelle für die ersten 302 Sekunden. Der identische dekodierte PCM-Präfix vor dem Mastering wurde per SHA-256 nachgewiesen. Ab 05:02 wurde der neue Schluss aus der bereits erzeugten Dienstfassung eingesetzt, mit einem 20-ms-Übergang. Das neue Schlussmaterial war im Player als MP3 mit 48 kHz verfügbar; es wurde auf 44,1 kHz angepasst. Die FLAC-/WAV-Ausgaben enthalten die bearbeiteten Samples verlustfrei, machen die MP3-Quelle des neuen Schlusses aber nicht nachträglich verlustfrei.

Anschließend wurde die gesamte Schnittfassung zurückhaltend technisch gemastert: 15-Hz-Hochpass, 5-ms-/20-ms-Randübergänge und linearer Lautheitsabgleich ohne zusätzliche Kompression oder Stereoverbreiterung.

| Messung | Ergebnis |
| --- | --- |
| Dauer | 5:37,974 |
| Format | Stereo, 44,1 kHz, 24 Bit |
| Integrierte Lautheit | −14,00 LUFS |
| True Peak | −2,03 dBTP |
| WAV/FLAC | Identisches dekodiertes 24-Bit-PCM verifiziert |

Details: [Mastering-Protokoll](shockT-project_Was-bleibt_Schluss-v2_Master_v2.mastering.json) und [Schnitt-Protokoll](edit-report.json). Das Master v1 bleibt erhalten.

## Noch zu prüfen

Der neue Gesang wurde automatisch gegen den Textvorschlag abgeglichen. Dabei bleiben einige Wörter um **05:02–05:06**, **05:09–05:11** und **05:13–05:16** unklar. Eine subjektive Prüfung von Stimme, Übergang und Wortlaut wurde nicht durchgeführt. Die Hörfassung ist daher noch nicht für einen Distributor oder für eine Liedtext-Einreichung freigegeben.

Die [Liedtextdateien v2](../lyrics/v2/lyrics.review.md) enthalten einen quellenbasierten Formatentwurf und die offenen Punkte. Eine tatsächliche Einreichung bei Musixmatch/Spotify ist nicht erfolgt.
