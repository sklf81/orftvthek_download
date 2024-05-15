![Download Executable](https://himbier.net/download/orftvthek_download/orftvthek_download)


# orftvthek_download
Ein Werkzeug um Videos aus der ORFTvthek herunterzuladen
## Installation
Dieses Programm kann man ganz einfach verwenden, indem man in der Konsole die mittels ``$python3 orftvthek_download.py`` das Skript ausführt.
### Build
Andernfalls kann man dieses Skript auch zu einer executable kompilieren.
In meinem Fall mache ich das mit _pyinstaller_. Zuerst muss man sich den pyinstaller installieren, dies geht am einfachsten mit dem Package-Installer für python "pip".
mit _pip_ kann man sich über die Konsole folgendermaßen den _pyinstaller_ installieren: ``$pip3 install pyinstaller``.
Mit dem _pyinstaller_ kann man mit folgendem Befehl eine executable kompilieren: ``$pyinstaller orftvthek_download.py --onefile``
Dafür muss man sich im "src"-Verzeichnis befinden.

Wenn das der pyinstaller fertig ist mit dem kompilieren, kann man unter src/dist die executable finden, die "orftvthek_download" heißen sollte.
Mit Doppelklick kann man dieses Programm ausführen und verwenden.

## Anwendung
Mit diesem Programm kann man Inhalte der ORFTVthek mit einer benutzfreundlichen Oberfläche einfach herunterladen.
!["Benutzeroberfläche"](images/UI.png)

Hierfür muss man lediglich die Internetaddresse des gewünschten Inhaltes in der oberen Programmzeile eingeben und dann dazu unten den gewünschten Dateinamen eingeben.
Wenn man dies getan hat, kann man auf "Download" klicken und das Video wird heruntergeladen.
## Funktionsweise
### Struktur
Im folgenden wird die Strukturiereung des Codes illustriert.
!["Schamtische Illustration"](images/schematic.png)
### Die Suche nach dem M3U8-Hyperlink
Die Funktion getM3U8Link dient dazu, aus einem gegebenen HTML-String den Link der M3U8 Datei für den gewünschten Stream zu finden.

Hierbei ist es nicht so einfach aus der ORFTvThek diesen Link herauszufinden. Bei händischer Unterscuhung kommt man darauf dass dieser sich in einem JSON-Container befindet, der sich unter:

```html
  <main class="main">
    ...
    <div class="mod_player html5">
      ...
      <div class="player_viewport ">
        ...
        <div class="jsb_ jsb_VideoPlaylist">
          <div class=" " data-jsb="{..}">
```
(Stand 15.05.2024) 

Im JSON-Container ``data-jsb`` befindet sich der M3U8 Link. Hierfür kann man den ganzen String innerhalb des Containers zu einem Python-Dictionary umwandeln und dann mittels entsprechender Indizierung den gewünschten Link erhalten.

>Dabei ist es wichtig anzumerken, dass die ORFTVthek sich in Zukunft ändern kann, was bedeuten würde, dass der M3U8-Link nicht mehr an derselben Stelle zu finden ist

Hierfür müsste man dann in der Funktion ``getM3U8Link(string, parameters)`` gegebenenfalls die parameter entsprechend ändern, oder im schlimmsten Fall auch das Verzeichnis des JSON-Containers, indem sich der Link versteckt. Hierfür ist es zu empfehlen, den Quellcode eines Streams in der TVThek mit den Browser-Entwicklertools zu untersuchen um den Link händisch auffinddig zu machen. Anhand dessen kann man dann ``getM3U8Link(string, parameters)`` auf den neusten Stand anpassen.


