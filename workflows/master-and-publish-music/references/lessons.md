# Belegte Verbesserungen

## 2026-10-21 – Spätere Credit-Freigaben haben Vorrang

Nach einer zunächst begrenzten Freigabe hat der Nutzer ausdrücklich erklärt, bei weiteren beauftragten Musikbearbeitungen keine Rücksicht auf vorhandene Credits nehmen zu wollen. Änderung: Aktuelle projektbezogene Freigaben berücksichtigen, statt die frühere Einzelgrenze oder wiederholte Credit-Rückfragen fortzuschreiben. Die Erlaubnis betrifft vorhandene Credits im beauftragten Ablauf; zusätzliche Käufe und neue Abonnements bleiben eigenständige Entscheidungen.

## 2026-10-21 – Folgeschritte können zusätzlich Credits kosten

Für eine Fortsetzung waren drei Credits genehmigt. Das anschließende „Get Whole Song“ berechnete einen weiteren Credit, obwohl das geöffnete Menü keinen Preis zeigte. Das überschritt den genehmigten Verbrauch und wurde dem Nutzer sofort gemeldet. Änderung: Gesamtkosten aller Teilschritte vor Auslösung prüfen; fehlende Preisangabe nicht als kostenlos werten. Ohne geklärte Kosten vorhandene Audiosegmente lokal zusammenfügen. Keine weiteren kostenpflichtigen Schritte nach einer unerwarteten Abbuchung.

## 2026-10-21 – Ausgangstext und gesungenes Ergebnis getrennt prüfen

Ein autorisierter MakeBestMusic-Text endete nach genau 5.000 Zeichen mitten im Wort. Der lokale ASR-Abgleich erkannte ebenfalls einen unvollständigen Schluss und produzierte in einer späten Instrumentalpassage zusätzlichen scheinbaren Text. Änderung: Ausgangstext nicht blind übernehmen, keine Schlusszeile erfinden, Instrumentalteile kontrollieren und Unsicherheiten separat dokumentieren. Textvorschläge und originalgetreue Spotify-Transkription bleiben getrennte Dateien.

## 2026-10-21 – Lautheit ist kein Ersatz für eine Klangbeurteilung

Eine geprüfte Quelle lag bereits bei −13,78 LUFS und −1,88 dBTP ohne Sample-Clipping. Daraus ergibt sich kein Bedarf für starke Kompression. Änderung: Bearbeitung pro Quelle begründen, technische Finalisierung klar als solche benennen und fehlende Hörprüfung ausdrücklich ausweisen. −14 LUFS bleibt eine mögliche Zielwahl, kein universeller Zwang.

## 2026-10-21 – Zweipass-Verfahren und Gegenprüfung

Die erste dynamische `loudnorm`-Analyse zeigte andere Ausgangswerte als das Ziel. Das explizit lineare Zweipass-Verfahren erreichte im separat gemessenen Export −14,00 LUFS und erhielt 5,0 LU LRA. Änderung: `normalization_type` prüfen und bei unerwarteter dynamischer Bearbeitung stoppen. Export separat messen; Analyse-Ausgabewerte nicht als finales Master-Ergebnis übernehmen.

## 2026-10-21 – FLAC und Git-Zugang prüfen

Ein 5:30-Stereo-Master ergab trotz FLAC etwa 64 MB. Änderung: Kompression nicht als Garantie für kleine Uploads behandeln. Binärdateien über einen geeigneten Git-Zugang übertragen und WAV/FLAC-Gleichheit anhand dekodierter PCM-Prüfsummen belegen. Authentifizierungsfehler in einer netzwerkbeschränkten Umgebung von tatsächlich ungültigen Zugangsdaten unterscheiden.

## 2026-10-21 – Kurzfassungen benötigen eigene Zeitleisten und Freigaben

Eine verkürzte Fassung konnte aus erhaltenen Textpassagen erstellt werden. Durch entfernte Wiederholungen und überlappende Übergänge änderten sich sowohl Liedtext als auch Zeilenzeiten. Änderung: Behaltene Quellbereiche und Überblendungen als Schnittplan speichern, Enddauer anhand der exportierten Frames prüfen und Liedtexte samt Zeitmarken pro Schnittversion neu ableiten. Die Bestätigung eines bereits vorhandenen Schlusses nicht als Freigabe neuer Übergänge ausgeben.

## 2026-10-21 – Aufbau und Refrain zusammen erhalten

Der Künstler beanstandete einen Übergang einer Kurzfassung: Der Aufbau versprach Energie, der entfernte Refrain ließ sie ausbleiben. Automatische Wortgrenzen und technische Pegelprüfungen hatten diesen musikalischen Fehler nicht erkannt. Änderung: Aufbau und erwarteten Refrain-Einsatz zusammen planen; Laufzeit bei Bedarf an einer anderen Wiederholung, im Vorspann oder in einer Brücke einsparen. Eine geänderte Fassung erneut als Hörentwurf vorlegen.

## 2026-10-21 – Generierungsdauer unabhängig messen

Eine auf 100 bis höchstens 108 Sekunden angeforderte Fortsetzung ergab Varianten von etwa 119 und 134 Sekunden. Die längere Variante wiederholte im Finale zudem eine laut ASR möglicherweise unvollständige Zeile. Änderung: Promptdauer als Wunsch behandeln; tatsächliche Laufzeit und Textvollständigkeit vor Montage prüfen, Restzeit aus Quellpräfix und Überblendungen berechnen und Überlänge nicht durch blindes Abschneiden gesungener Wörter beheben.
