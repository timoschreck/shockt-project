# Was bleibt – technisches Master v1

Künstler: **shockT project**. Erstellt am 21.10.2026.

Die Quelle ist eine Stereo-WAV mit 44,1 kHz und 16 Bit, Dauer 5:30,481. Sie lag bereits bei −13,78 LUFS, −1,88 dBTP und 5,0 LU LRA. Die Sample-Prüfung fand keine übersteuerten Samples.

## Bearbeitung

- Zurückhaltender Hochpass bei 15 Hz gegen DC-/Subsonic-Anteile.
- Randübergänge von 5 ms am Anfang und 20 ms am Ende; keine Kürzung des Songs.
- Zweipass-Lautheitsabgleich mit linearem Gain auf −14 LUFS. Keine zusätzliche Kompression, kreative EQ-Bearbeitung oder Stereoverbreiterung.
- Export als 24-Bit-WAV und verlustfreies 24-Bit-FLAC bei unveränderter Abtastrate. Die 24-Bit-Ausgabe bewahrt die Rechengenauigkeit der Bearbeitung; sie ergänzt keine in der 16-Bit-Quelle fehlenden Informationen.

## Verifikation

Das finale Master wurde separat erneut gemessen: **−14,00 LUFS**, **−1,95 dBTP**, **5,0 LU LRA**. Der SHA-256-Vergleich des dekodierten 24-Bit-PCM belegt, dass FLAC und WAV identisches Audio enthalten. Die Original-Prüfsumme blieb unverändert. Details und Dateiprüfsummen: [mastering-report.json](mastering-report.json).

Es handelt sich um ein konservatives technisches Master. Eine subjektive Hörprüfung wurde nicht durchgeführt; klangliche Freigabe durch den Künstler steht deshalb aus.

Das gewählte Lautheitsziel orientiert sich an [Spotifys Mastering-Hinweisen](https://support.spotify.com/mx-en/artists/article/loudness-normalization/). Es ist keine allgemeine Zulassungsvoraussetzung für Musikdistribution.
