# Was bleibt? – Wortlaut- und Synchronisationsprüfung v1

Status: **Entwurf, nicht zur Einreichung freigegeben**. Bezug: bestehendes Master v1, Dauer 5:30,481. Prüfung am 21.10.2026.

## Vorliegende Belege

Der passende MakeBestMusic-Track ist [Was bleibt?](https://makebestmusic.com/app/shared-music/7ec76335-650e-498b-b031-8c802d544a00). Titel und angezeigte Dauer stimmen mit dem gelieferten Song überein. Der angezeigte Ausgangstext endet nach genau 5.000 Zeichen mitten in `Nicht, wer lau`. Zwei lokale ASR-Durchläufe (`small` und `large-v3-turbo`) wurden mit dem WAV-Master abgeglichen; die Textdateien sind ausdrücklich Rohentwürfe.

## Offene Stellen

| Bereich | Befund | Konsequenz |
| --- | --- | --- |
| 0:06–0:17 | Bei „Vier Zeiten / Vier Leben“ schwankt ASR zwischen „vier“ und „viel“ | Gegen die Stimme prüfen; Ausgangstext allein genügt nicht |
| 0:41–0:45 | „Sneaker auf Pump“ und folgende Zeile werden unterschiedlich erkannt | Wortlaut gegenhören |
| 0:59–1:03 | Starke Abweichung beim letzten Wort des Pre-Hooks; stärkeres Modell erkennt das explizite Wort des Ausgangstexts | Keine automatische Zensur oder Ersetzung |
| 1:03–1:07 | „Schnitt / Stück / Narben“ mit Erkennungsfehlern | Wortlaut prüfen |
| 1:38–1:42 und 2:45–2:50 | Schlusszeile des Refrains undeutlich erkannt | Wiederholungen einzeln abgleichen |
| 2:59–3:07 und 4:31–4:49 | Mehrere dicht gerappte Zeilen mit Abweichungen | Besonders Pronomen, Negationen und Zeilenenden prüfen |
| 3:50–4:02 | Beide ASR-Läufe erkennen eine Wiederholung der letzten Bridge-Zeile, die im Ausgangstext nicht wiederholt ist | Zusätzliche Wiederholung in der tatsächlichen Transkription berücksichtigen |
| 4:05–4:25 | Ausgangstext sieht „Was bleibt? / Wer hält? / Wer geht? / Wer fällt?“ vor; ASR bestätigt dies nicht vollständig | Nicht ungeprüft aus dem Eingabetext übernehmen |
| 4:52–5:04 | Finale drei vollständige Zeilen und ein Schlussfragment erkannt; Modelle liefern beim Fragment unterschiedliche Wörter | Ausgangstext und Aufnahme zeigen Prüfbedarf. Keine fehlende Schlusszeile erfinden |
| 5:21–5:30 | Die Modelle erzeugen widersprüchliche kurze Phrasen in der späten Outro-Passage | Als mögliche ASR-Halluzination behandeln; nicht automatisch in Liedtext aufnehmen |

## Dateien

- `lyrics.source-reference.draft.txt`: Ausgangstext ohne Produktionsanweisungen, einschließlich des sichtbaren abgebrochenen Fragments. Keine Behauptung, dass jede Zeile so gesungen wurde.
- `asr-small.draft.txt` und `asr-large-v3-turbo.draft.txt`: automatische Audio-Transkriptionsbeobachtungen mit Segmentzeiten; fehlerhafte Wörter bewusst nicht als vermeintlich geprüft korrigiert.
- `lyrics.alignment.draft.json`: Kandidaten zum Wort-/Zeilenabgleich. Deckungsgrad ist keine Zuverlässigkeitsgarantie.
- `lyrics.sync.partial.draft.lrc`: unvollständige, ungeprüfte Zeitanlage aus übereinstimmenden Wörtern. Die unsichere Zwischenpassage und das Schlussfragment haben keine freigegebenen Zeitmarken. Nicht als fertige Synchronisation importieren.
- `lyrics.metadata.json`: Audiozuordnung und getrennte Prüf-/Einreichungsstatus.

Eine subjektive Hörprüfung oder Künstlerfreigabe wurde bisher nicht durchgeführt. Es wurden keine Liedtexte an Musixmatch oder Spotify übermittelt.

## Redaktionelle Reparatur

Für einen neuen Schluss liegt getrennt der [v2-Textvorschlag](../../edits/v2-ending-lyrics.txt). Dieser ist neu geschrieben und gehört erst nach entsprechender Audio-Neugenerierung zur neuen Fassung. Er ist kein nachträglich erfundener Bestandteil von v1.
