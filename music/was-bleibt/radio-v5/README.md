# Was bleibt? – Radiofassung v5: Stimmangleichung

**3:49,728 Minuten. Technisch geprüfte Hörfassung; klangliche Freigabe offen.**

Der Künstler fand den v4-Schluss musikalisch besser, hörte am Anschluss aber weiterhin eine andere Stimmlage/Stimmfarbe. Diese Bearbeitung verändert gezielt den Klangkörper der Schlussstimme, statt die gesamte Musik oder Gesangsmelodie zu transponieren.

## Quellen und Bearbeitung

Die bereits in MakeBestMusic vorhandenen Quellaufnahmen Radio-v3(2) und Radio-v4-Schluss(1) wurden über die interne Bibliothek im Normal-Stem-Splitter getrennt (zweimal fünf vorhandene Credits; 2753 → 2743; kein Kauf). Der Upload der lokalen Gesamtfassung wurde nicht abgeschlossen. Stem-WAV-Dateien bleiben lokal und werden nicht zusätzlich im Repository veröffentlicht.

Ein grober Autokorrelationsvergleich der isolierten Stimmen zeigt in den gewählten unterschiedlichen Gesangspassagen denselben Median der erkannten Grundfrequenz, etwa 178 Hz. Er beweist weder identische Melodie noch Sängeridentität. Die Schlussstimme ist in diesem Vergleich spektral heller. Deshalb ist v5 ein konservativer **Klangfarbenversuch mit Formantverschiebung um nominal −1,5 Halbtöne**, bei rechnerisch unveränderter Gesamthöhe und Dauer. Umsetzung: abgesenkte Wiedergaberate plus gegenläufige Rubberband-Korrektur von Tempo/Tonhöhe mit Formanterhaltung. Separater RMS-Abgleich des bearbeiteten Gesangs.

Die Korrektur wird als Differenz aus bearbeitetem und ursprünglichem Vocal-Stem dem vorhandenen v4-Mix zugefügt. Das separierte Instrumental-Residuum wird nicht ersetzt, transponiert oder neu arrangiert. Instrumentenanteile, die in den Gesangs-Stem durchschlagen, können dennoch mitbearbeitet werden; Trenn- und DSP-Artefakte sind hörzuprüfen. Das ist keine Voice-Conversion und kein Nachweis derselben Sängeridentität.

## Prüfungen

- Erste **190 Sekunden PCM-identisch** zu v4; gesprochene Einleitung und bestätigter Beginn unverändert.
- **Gleiche Framezahl und Dauer** wie v4, Stereo 44,1 kHz, 24 Bit, weiterhin unter 3:50.
- Grobe Grundfrequenz-Mediane und Quartile vor/nach Bearbeitung gleich; beste Korrelation der 10-ms-Lautheitshüllkurven bei **0 ms Versatz**, etwa 0,990. Das ist keine vollständige Noten- oder Hörprüfung.
- Final separat gemessen: **−14,25 LUFS**, **−2,54 dBTP**. Keine globale Lautheitsänderung des bestätigten Anfangs.
- WAV/FLAC auf identisches dekodiertes PCM geprüft, Quelldateien unverändert.

Siehe Messprotokoll, `edit-report.json`, `voice-analysis.json` und `voice-processing-check.json`. Eine DSP-Rundung um ein Sample am Ende der bearbeiteten Einzelstimme wurde ausgeglichen; die finale Dauer bleibt exakt erhalten.

## Hörprüfung und Text

Bitte besonders ab **03:11** prüfen, ob die Schlussstimme näher an die vorangehende Stimme rückt und ob Zischlaute, Chor, Ausklang oder Stimmübergang durch die Bearbeitung leiden. Der Agent hat keine subjektive Hörprüfung durchgeführt; die moderate Einstellung ist ein Vorschlag für die Künstlerprüfung.

Liedtext und nominale Zeitleiste werden aus v4 als Entwürfe übernommen. Keine Wörter wurden absichtlich geändert oder neu erzeugt. Alle offenen Wortlaut- und Synchronisationsfragen bleiben bestehen. Keine Übermittlung an Spotify, Musixmatch oder Distributor. Quellen haben weiterhin die in v4 dokumentierten MP3-Anteile; WAV/FLAC rekonstruieren keine verlorene Quellinformation.
