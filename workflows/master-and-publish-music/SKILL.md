---
name: master-and-publish-music
description: Master songs, transcribe and prepare lyrics for Spotify/Musixmatch, verify exports and publish finished files to a chosen repository. Use for repeated music mastering, lyrics and upload workflows across projects.
---

# Musik mastern, Liedtexte vorbereiten und ablegen

Dieser persönliche Skill gilt projektübergreifend für beauftragte Musikbearbeitung. Der Nutzerwunsch ist: **bereitgestellte Songs zuerst angemessen mastern und prüfen, erst danach die fertigen Versionen hochladen; zu jedem verfügbaren Song außerdem einen originalgetreuen Liedtext für Spotify vorbereiten und im Projekt-Repository ablegen**. Er erteilt keine pauschale Erlaubnis für neue Veröffentlichungsziele, kostenpflichtige Dienste oder Änderungen an Konten und DNS.

## Projekt und Quelle feststellen

Aktuelle Projektanweisungen, Dateipfade, Künstlernamen und Veröffentlichungsziele prüfen. Vorhandene Dateien und Repository-Inhalte lesen, bevor fehlende Angaben erfragt werden. Keine Künstlernamen, Ziele oder Zugangsdaten aus einem anderen Projekt übernehmen. Wenn ein Repository genannt wird, dessen Sichtbarkeit beachten; öffentliches GitHub bedeutet öffentliche Verfügbarkeit der Audiodateien.

Original unverändert erhalten und mit SHA-256 identifizieren. Neue Ausgaben eindeutig nach Titel und Version benennen. Keine vorhandenen Master überschreiben. Rohdateien, persönliche lokale Pfade und Zugangsdaten nicht automatisch mit veröffentlichen.

## Bearbeitung pro Song entscheiden

Format, Dauer, Abtastrate, Kanäle und Bit-Tiefe feststellen. Integrierte Lautheit, True Peak und LRA messen; zusätzlich, soweit sinnvoll, Sample-Clipping, DC, Anfang/Ende und Stereoverträglichkeit prüfen. Wenn Hörwerkzeuge verfügbar sind, repräsentative Stellen und Übergänge bei angeglichener Lautheit abhören. Hörprüfungen nicht behaupten, wenn nur Messungen vorliegen.

Technische Messwerte belegen keine textliche Vollständigkeit. Hinweise auf abgebrochene Gesangszeilen vor einer Release-Freigabe prüfen. Ein technisch geprüftes Master mit offenen Text-/Klangfragen als Hörfassung kennzeichnen; technische Fertigstellung, Repository-Ablage und Veröffentlichungsfreigabe auseinanderhalten.

Zielpegel und Bearbeitung aus Material, Stil und Nutzerziel ableiten. Für eine konservative Streaming-Fassung können etwa −14 LUFS und höchstens −1 dBTP passen; dies ist weder universelles Mastering-Ziel noch Upload-Pflicht. Aktuelle Plattformvorgaben bei Bedarf aus offiziellen Quellen verifizieren.

Messungen allein rechtfertigen keinen kreativen EQ, keine Stereoverbreiterung oder starke Kompression. Bereits passende Quellen nur gering bearbeiten und den Umfang ehrlich benennen. Subsonic-Filter und Rand-Fades nur anwenden, wenn begründet; keine leisen Passagen oder Ausklänge automatisch wegschneiden. Eine Lautheitsanpassung nicht als umfassende klangliche Überarbeitung darstellen.

Vorhandene Werkzeuge verwenden. Bei Bedarf FFmpeg über ein seriöses Paket wie `imageio-ffmpeg` installieren, isoliert vom Repository. Keine binären Werkzeuge oder Paketordner committen. Für PCM-WAV-Quellen kann [scripts/master_wav.py](scripts/master_wav.py) Zweipass-Messung, konservative Bearbeitung und Verifikation übernehmen. Parameter pro Song wählen, nicht blind Standardwerte anwenden. Bei fehlender Peak-Reserve stoppt das Skript, statt unbemerkt auf dynamische Normalisierung zu wechseln.

## Kurzfassungen und neue Schnittversionen

Bei einem Laufzeitlimit zunächst einen nachvollziehbaren Schnittplan aus der vorhandenen Aufnahme erstellen. Vollständige Textgedanken und musikalische Phrasen erhalten; wiederholte Refrains, lange Vor-/Nachspiele und Zwischenpassagen als Kürzungskandidaten prüfen. Keine Beschleunigung oder Neugenerierung nur zum Einhalten der Dauer, sofern ein sinnvoller Schnitt ausreicht.

Behaltene Quellbereiche, Ausgabezeiten und jede Überblendung dokumentieren. Die endgültige Dauer aus den tatsächlich exportierten Frames prüfen; Überblendungszeiten verkürzen die Gesamtlaufzeit zusätzlich. Neue Übergänge gesondert prüfen und nicht aus einer früheren Freigabe anderer Passagen als genehmigt ableiten. Auch ein für sich bestätigter Schluss kann in einem anderen Arrangement unpassend wirken. Bei einer Schlussreparatur die tatsächlich davor verwendete Aufnahme als Fortsetzungsquelle wählen. Bestätigte Bereiche nach Möglichkeit unverändert übernehmen und bei zugesagter Erhaltung deren PCM-Gleichheit prüfen; Anpassungen auf den neuen Abschnitt begrenzen. Vor einem Refrainschnitt prüfen, ob der vorausgehende Aufbau gerade diesen Energieeinsatz erwarten lässt. Ein erhaltener Textgedanke und eine kurze Überblendung reichen nicht aus: Aufbau, Refrain-Einsatz und musikalische Auflösung als Einheit behandeln; nötigenfalls an anderer Stelle kürzen.

Liedtext und Zeitmarken pro Schnittversion neu ableiten: entfernte Wiederholungen und Strophen auch im Text entfernen, Zeilenzeiten anhand der Schnittzeitleiste inklusive Überlappungen umrechnen und anschließend am finalen Audio prüfen. Automatisch umgerechnete Zeitmarken bleiben bis zur Hörprüfung Entwürfe. Jede neue Schnittfassung separat mastern, messen und versionieren.

## Liedtexte und Textüberarbeitung

Für verfügbare Songs Original-Liedtexte aus bereitgestellten Dateien oder dem vom Nutzer autorisierten Musikprojekt beziehen, beispielsweise aus MakeBestMusic. Das passende Audio und die genaue Version abgleichen. Ausgangstext ist eine Referenz, kein Nachweis des tatsächlich Gesungenen. Auffällige Längengrenzen, abgebrochene Wörter, zusätzliche Wiederholungen und geänderte Zeilen ausdrücklich prüfen. Keine fehlenden Schlusswörter anhand von Reim oder Thema als Transkription erfinden.

Den aktuellen Weg und die Formatvorgaben anhand [references/spotify-lyrics.md](references/spotify-lyrics.md) und der dort verlinkten offiziellen Quellen prüfen. Liedtexte und Zeitmarken aus dem tatsächlich veröffentlichten oder vorgesehenen finalen Audio gewinnen. Lokale ASR kann einen Entwurf liefern; niedrige Wortwahrscheinlichkeiten, Instrumentalpassagen, abrupte Sprachwechsel und Widersprüche zum Ausgangstext gesondert prüfen. ASR-Ausgabe ist keine Hörfreigabe. Bei einem Musikprojekt mit vielen Entwürfen den relevanten Katalog abgrenzen; nicht beiläufig alle Entwürfe als Veröffentlichungen behandeln.

Für lokale ASR steht [scripts/transcribe_local.py](scripts/transcribe_local.py) zur Verfügung. Es benötigt `faster-whisper`, NumPy und FFmpeg, lädt gegebenenfalls das gewählte freie Modell und gibt ausdrücklich ungeprüfte Rohtexte mit Wortzeitmarken aus. Audio bleibt lokal. Der FFmpeg-Dekodierweg vermeidet eine beobachtete Inkompatibilität zwischen dem Audio-Leser aktueller Paketversionen. Für Schluss-/Problemstellen kann `--clip` einen begrenzten zweiten Abgleich erzeugen.

Im Songordner sauberen UTF-8-Liedtext, bei Bedarf eine zeitmarkierte Arbeitsfassung sowie eine getrennte Review-/Statusdatei ablegen. Ungeprüfte Dateien ausdrücklich `draft` nennen. Hinweise, alternative Wörter, Sprecher-/Produktionsanweisungen und Unsicherheiten gehören in die Review-Datei, nicht in einen zur Einreichung bestimmten Liedtext. LRC ist eine Arbeits-/Austauschdatei; nicht behaupten, dass Musixmatch sie automatisch importiert. Zeitmarken müssen am finalen Audio überprüft werden.

Status unterscheiden: Referenztext vorhanden, Audioentwurf transkribiert, Wortlaut geprüft, Synchronisation geprüft, Künstlerfreigabe, beim Anbieter übermittelt, auf Spotify sichtbar. Ein Repository-Upload erfüllt nur die Ablage. Keine Übermittlung oder Freigabe behaupten, bevor der jeweilige Schritt tatsächlich erfolgt ist. Fehlende Audiodateien im Katalog als offen führen; keine Vollständigkeit über unbekannte Songs behaupten.

Auf Wunsch Texte redaktionell verbessern oder fehlende Passagen als **eigene Vorschläge** schreiben. Diese Bearbeitung separat versionieren. Ein ergänzter Text passt erst nach entsprechender Gesangs-/Audioüberarbeitung zur neuen Aufnahme. Keine neuen Wörter in Spotify-Transkripte einer unveränderten Aufnahme einfügen. Eine neue Gesangsaufnahme oder gezielte Neugenerierung kann nötig sein; dafür Kosten, Werkzeugfähigkeit, Übergänge und Rechte im konkreten Auftrag klären. Mastering ändert keine gesungenen Wörter.

Bei einer ausdrücklich beauftragten Neugenerierung zuerst Einsetzpunkt, Ersatztext und vorhandene Credit-/Budgetfreigabe feststellen. Eine ausdrückliche Freigabe, vorhandene Credits ohne Rücksicht auf deren Verbrauch zu nutzen, gilt auch für nötige Varianten, Zusammenfügen und Exporte im beauftragten Musikablauf. Dafür keine erneuten Credit-Freigaben verlangen und Credits nicht als Qualitätsbremse behandeln. Solche Freigaben projekt- beziehungsweise kontobezogen dokumentieren; sie erlauben keine unangewiesenen endlosen Generierungen und keinen zusätzlichen Kauf von Guthaben oder Abonnements.

Wenn ein konkretes Limit gilt, alle nötigen Teilschritte darin berücksichtigen. Eine fehlende Preisangabe ist kein Nachweis, dass ein Schritt kostenlos ist. Bei unklaren Kosten außerhalb der bestehenden Freigabe vor Auslösung klären oder vorhandene Audiodateien lokal zusammenfügen. Ein begrenzter Generierungspreis autorisiert keine darüber hinausgehenden Credits für spätere Schritte. Nicht gedeckten Verbrauch sofort offenlegen und weitere solche Schritte stoppen. Generierte Varianten nach Textvollständigkeit, Stimm-/Klangkontinuität, Übergängen und Ausklang prüfen; Künstlerfreigabe bleibt getrennt. Eine im Prompt genannte Dauer ist keine verlässliche Begrenzung. Tatsächliche Segmentdauer und Gesamtlaufzeit inklusive Quellpräfix und Überblendungen messen; bei Überlänge keine gesungenen Zeilen ungeprüft abschneiden.

## Export und Veröffentlichung

Verlustfreies WAV für Distribution bereitstellen, Abtastrate ohne Grund nicht erhöhen. 24-Bit-Export nach DSP verbessert die Ausgabepräzision, rekonstruiert keine verlorene Quellauflösung. FLAC kann für die Repository-Ablage dieselben PCM-Samples verlustfrei speichern; der Künstler muss WAV weiterhin erhalten oder verlustfrei daraus erzeugen können.

Finale Datei unabhängig erneut messen und gewähltes Lautheits-/Peak-Ziel überprüfen. Dauer, Kanäle, Abtastrate und dekodierte Framezahl prüfen; FLAC/WAV auf identisches dekodiertes PCM vergleichen. Original-Prüfsumme erneut prüfen. Bearbeitungen, gemessene Vorher-/Nachherwerte, tatsächliche Prüfungen und offene Hörfreigabe dokumentieren. Behauptete Ergebnisse müssen aus dem aktuellen Lauf stammen.

Erst nach bestandenen technischen Prüfungen ins autorisierte Ziel hochladen. Repository-Regeln sowie Grenzen für Dateigröße und Authentifizierung prüfen. FLAC ist nicht zwangsläufig klein genug für Browser-Uploads. Für große Dateien vorhandenen Git-Zugang verwenden; keine bezahlten Speicheroptionen ungefragt aktivieren. Nur die beauftragten Master, Liedtexte und nötigen Protokolle committen. Liedtextentwürfe dürfen zur Prüfung abgelegt werden, wenn ihr Status klar erkennbar ist. Remote-Dateien nach Upload verifizieren. Bei einem Fehler den überprüften lokalen Master erhalten und den konkreten Blocker nennen.

Den Nutzer knapp über Bearbeitungsumfang, Ergebnis, tatsächlichen Uploadstatus und offene Klangbeurteilung informieren; spielbare lokale Datei und Repository-Link liefern, soweit möglich.

## Nach jedem Durchlauf verbessern und speichern

Zum Abschluss **immer** prüfen: Wo gab es eine belegte Fehlentscheidung, unnötige Wiederholung, Exportabweichung, fehlende Prüfung oder neue Nutzerpräferenz? Den tatsächlichen Verlauf und die Ergebnisse heranziehen. Die bisherigen [Lernerfahrungen](references/lessons.md) nur bei passendem Anlass lesen.

Bei einem belegten, wiederverwendbaren Verbesserungsbedarf diesen Skill oder sein Hilfsskript gezielt aktualisieren und im persönlichen Skill-Verzeichnis erneut speichern. Das ist vom Nutzer für diesen Skill gewünscht. Echte neue Erkenntnisse mit Datum, Beobachtung und praktischer Änderung knapp in `references/lessons.md` aufnehmen; Dopplungen zusammenführen. Keine Geheimnisse, Audiodaten, personenbezogenen Projektinhalte oder konkreten privaten Pfade in den globalen Skill übernehmen.

Keine Änderung nur um einer Änderung willen. Wenn keine belegte Verbesserung vorliegt, bestehende Fassung erhalten; keinen leeren Verlaufseintrag erzeugen. Keine Berechtigungsgrenzen lockern, keine Erfolgsbelege erfinden und keine anderen Skills oder Projekte automatisch ändern. Kosten, externe Schreibaktionen oder neue Ziele sind nicht durch Selbstverbesserung autorisiert.

Geänderte Skripte an einem passenden lokalen Beispiel auf ihre relevanten Audio-Invarianten prüfen und die Skill-Dateien mit dem verfügbaren Skill-Validator prüfen. Bei gesperrtem Ziel die fertige Revision lokal behalten und den Speicherblocker konkret nennen. Eine Änderung erst nach erfolgreichem Speichern als gespeichert melden.
