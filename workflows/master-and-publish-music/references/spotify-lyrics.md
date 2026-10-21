# Spotify-Liedtexte vorbereiten

Quellenstand: 21.10.2026. Bei einer tatsächlichen Einreichung erneut prüfen.

## Offiziell belegter Weg und Kernregeln

[Spotify: Managing your lyrics](https://support.spotify.com/cg-en/artists/article/managing-your-lyrics-on-spotify/) nennt Musixmatch als Anbieter. Ein verifiziertes Künstlerprofil und der kostenlose Musixmatch-Pro-Tarif ermöglichen die Bearbeitung. Der Weg führt über Roster, Song, Lyrics beziehungsweise Sync und anschließend Send. Die Anzeige auf Spotify kann danach einige Tage dauern.

Nur tatsächlich gesungenen beziehungsweise lyrisch gesprochenen Inhalt erfassen. Wiederholungen vollständig ausschreiben, keine Multiplikatoren. Originalschrift verwenden und Abschnitte mit unterstützten Tags wie `#VERSE` und `#CHORUS` kennzeichnen. Synchronisation am ersten gesungenen Wort jeder Zeile ausrichten; die Hauptstimme priorisieren.

Spotify verweist für Details auf die [Musixmatch-Richtlinien](https://community.musixmatch.com/guidelines). Diese Seite war beim Quellenabruf nicht erreichbar. Nicht aus älteren Erinnerungen zusätzliche zwingende Zeichensetzungs- oder Importregeln ableiten; solche Details im aktuellen Anbieter-Editor prüfen. Ein LRC-Arbeitsexport belegt keine Musixmatch-Importfunktion.

## Arbeitsdateien und Freigabestatus

- `lyrics.musixmatch.draft.txt`: formatierter Entwurf; keine internen Kommentare im Text.
- `lyrics.sync.draft.lrc`: optionale Zeitmarkenfassung zur Prüfung, an dieselbe Audioversion gebunden.
- `lyrics.review.md`: Quellen, unsichere Wörter, ausgelassene oder zusätzliche Passagen, Ende der Audiodatei, Freigabestatus und mögliche Korrekturvorschläge.
- `lyrics.metadata.json`: Quelle/Audioprüfsumme, Modell und Datum, bekannte Track-IDs sowie getrennte Status für Wortlaut, Synchronisation und Einreichung. Unbekannte ISRC/Track-IDs nicht erfinden.

Nur eine vollständig geprüfte und zur Aufnahme passende Fassung als einreichungsbereit kennzeichnen. Redaktionelle Alternativen in einer separaten Datei halten. Sie sind keine Transkription und brauchen bei Übernahme eine entsprechende Audiofassung.

## Praktischer Quellenabgleich

MakeBestMusic-Ausgangstexte können Produktionsanweisungen, ungesungene Tags und abgeschnittene Zeilen enthalten. Die Audiodauer und der Titel helfen beim Zuordnen, ersetzen aber nicht den Audioabgleich. Bei einer auffälligen Textlänge oder einem abgebrochenen Wort Ende gegen die Aufnahme prüfen. ASR-Halluzinationen in Instrumentalteilen nicht übernehmen. Wenn nur der Ausgangstext verfügbar ist, eine Referenzfassung sichern und den Status Audioabgleich offen setzen.
