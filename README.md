# InGefAufgabe

## Beschreibung
Ein einfacher HTTP-Server mit 2 Endpunkten, die über den Port 8080 zu erreichen sind.
Die Logs werden in der Datei logfile.log gespeichert.
Detaillierte Informationen zu den Endpunkten und die Möglichkeit zum Testen, sobald der Server läuft, finden sich hier:

http://127.0.0.1:8080/docs


## Dockerfile
Das sind die Command-Line Befehle um das Docker Image zu bauen und zu starten:

```
docker build -t myimage .
docker run -d --name mycontainer -p 8080:8080 myimage
```

## Bekannte Probleme
- Der Server liest die zum Endpunkt /stats/ gesendete Datei mit dem Encoding des Clients. Beim Testen war das ein
Windows-PC, deshalb ist das Encoding auf 'cp1252' gesetzt. Wenn der Client ein anderes Encoding verwendet, kann die
CSV-Datei nicht verarbeitet werden.