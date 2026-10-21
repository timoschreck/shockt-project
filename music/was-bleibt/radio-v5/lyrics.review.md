# Liedtextprüfung – Radiofassung v5

Stand: 21.10.2026. **Arbeitsfassung, noch nicht einreichen.**

## Aufnahme und Zuordnung

Dieser Text gehört ausschließlich zur Radiofassung v5 (3:49,728). Audio: `shockT-project_Was-bleibt_Radiofassung_Stimmangleichung_Master_v5.flac`, SHA-256 `e7146b8d25c132fe4df267ba029082576fffca29ee3e77b442e0ee3aa15ebb06`.

Künstler: **shockT project**, Spotify-Künstler-ID `4RFOjLyMP38HzOOcZgXJsd`. Für diese Aufnahme sind Spotify-Track-ID, ISRC und Veröffentlichungstermin noch nicht belegt. Keine Zuordnung zu einem anderen Song oder einer längeren Fassung übernehmen.

## Dateien und Aussagekraft

- `lyrics.musixmatch.draft.txt`: bisheriger Referenztext aus der Schnitt-/Generierungsplanung. Er belegt nicht jedes tatsächlich gesungene Wort oder die Anzahl der Wiederholungen.
- `lyrics.sync.partial.asr-draft.lrc`: ältere, partielle Zeitmarken mit erkennbaren ASR-Fehlern. Historische Arbeitsdatei; nicht zur Einreichung verwenden.
- Ein neuer vollständiger lokaler Audioabgleich der v5 ist separat als `radio-v5-full.asr-draft.json` und `.txt` abgelegt. `lyrics.sync.full.asr-draft.lrc` enthält seine Segmentanfänge; das sind noch keine manuell geprüften Einsätze jeder einzelnen Liedtextzeile. Auch dieser ist automatische Spracherkennung, keine bestätigte Transkription.

## Bereits erkennbare Prüfpunkte

| Stelle ungefähr | Offene Frage |
| --- | --- |
| 00:06–00:18 | Alle fünf gesprochenen Einleitungszeilen und deren genaue Einsätze erfassen. In der alten LRC fehlt „Vier Leben.“; der Einsatz von „Was bleibt?“ ist widersprüchlich. |
| 00:46–00:54 | „Schnitt“ / „Narben“ und die genaue Zeilenaufteilung prüfen; automatische Erkennung weicht ab. |
| 01:17–01:26 | Die Schlusszeile des ersten Refrains fehlt in der alten LRC. Tatsächlichen Wortlaut und Einsatz prüfen. |
| 01:51–02:02 | „Brust voll Druck, doch nannten’s Freiheit“ fehlt in der alten LRC. |
| 02:02–03:10 | Die automatisch erkannten Wörter „Rack“, „Vorzeile“, „steckt“, „familiär“ und „Abstoß“ widersprechen dem Referenztext. An der Aufnahme prüfen, keine blinde Ersetzung. |
| Ab 03:11 | Genau prüfen, ob „Heute weiß ich“ vollständig gesungen wird und welche Wiederholungen nach „lässt dich nicht allein“ tatsächlich vorkommen. |
| 03:28–Ende | Der Referenztext nennt nur „Was bleibt? / Wer bleibt.“; die alte ASR erkennt zusätzliche Wiederholungen und ein unsicheres Schlusswort. Keinen Schluss aus älteren Versionen als bestätigt übernehmen. |

## Einreichung vorbereiten

Nach dem Wortlautabgleich Wiederholungen vollständig ausschreiben, nur lyrisch gesprochene/gesungene Inhalte erfassen und die Zeilen am ersten gesungenen Wort synchronisieren. Keine ASR-Kommentare oder Unsicherheitsmarker in den eigentlichen Liedtext übernehmen. LRC bleibt eine Arbeitsdatei; eine Importfunktion ist nicht bestätigt.

Die Künstlerfreigabe bei Musixmatch steht noch aus. Eine technische Fehlermeldung im Verteilungsbereich ist kein Beleg für eine erfolgreiche Einreichung. Es wurden keine Liedtexte übermittelt. Die klangliche Freigabe des neuen v5-Schlusses sowie die vollständige Wortlaut- und Synchronisationsprüfung bleiben offen.

Offizielle Vorgaben am 21.10.2026 erneut geprüft: [Spotify – Managing your lyrics](https://support.spotify.com/cg-en/artists/article/managing-your-lyrics-on-spotify/). Der kostenlose Musixmatch-Tarif reicht laut Spotify für das Hinzufügen, Bearbeiten und Synchronisieren aus. Der weiterführende Musixmatch-Richtlinienlink war beim Webabruf nicht erreichbar; daraus keine zusätzlichen Formatpflichten ableiten.

## Ergebnis des erneuten Audioabgleichs

Das große lokale Modell hat die tatsächliche v5-Datei vollständig verarbeitet; der Schluss wurde mit einem zweiten lokalen Modell zusätzlich geprüft. Die Prüfungen ändern weder Aufnahme noch Referenztext. Modellübereinstimmung ersetzt keine Hörfreigabe.

- Die bisher fehlende zweite Einleitungszeile wird bei etwa 00:09 erkannt, allerdings als „Viel Leben“ statt Referenz „Vier Leben“. Wortlaut hörprüfen.
- „Was bleibt?“ in der Einleitung wird neu bei etwa 00:16,38 erkannt; die ältere LRC nennt 00:14,06. Kein bestätigter Sync-Wert.
- Die erste Refrain-Schlusszeile ist bei etwa 01:21 erfasst, aber mit unplausibler Erkennung. Referenzwortlaut bleibt offen.
- Die vorher fehlende Zeile „Brust voll Druck, doch nannten’s Freiheit“ wird bei etwa 01:54 erkannt.
- Das große Modell erkennt „Heute weiß ich, was noch gilt“ ab etwa 03:09,80, also schon vor dem nominalen Stimmkorrekturbeginn. Der alte LRC-Einsatz bei 03:11,21 und ihr verkürzter Wortlaut dürfen nicht als geprüft gelten.
- Beide Modelle erkennen ab etwa 03:28,85 dreimal „Was bleibt“. Das große Modell erkennt eine weitere Wiederholung ab etwa 03:36,40; das kleine Modell erfasst diese nicht. Keines bestätigt danach die Referenzzeile „Wer bleibt“. Das belegt keine Abwesenheit: Ausklang ab 03:28 bis zum Dateiende persönlich abhören.

Es gibt weiterhin Abweichungen im übrigen Text. Die neue vollständige LRC ersetzt nur die bisher lückenhafte automatische Arbeitsgrundlage, keine endgültige Transkription. Keine automatische Ersetzung unklarer Wörter durch erwartete Reime oder Referenzzeilen.
