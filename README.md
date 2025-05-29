_____________________________________
-------------------------------------
|| __ .. ** REKLÁMFIGYELŐ  ** .. __ ||
 -----------------------------------
Készítette: ECSEDI TAMÁS

--------
-- PROJEKT --
------

Listázza YouTube-ról a ma feltöltött magyar videókat.
A videók hanganyagait lementeni szövegbe.
A szövegben ellenőrzi, hogy a keresett kulcsszó szerepel-e.


--------
-- PROTOTIPUS --
------

run_all.bat     >> futtatja a projektet Windowson, ami áll:

ytScrapper5     >> listáz max 5 db ma vagy tegnap megjelent magyar YT videót
                >> a video_Scrapper.txt fájlba

ytSpeechToText  >> a listázott videókból .mp3 csinálunk
                  >>  (a demoban a video_textToSpeech.txt használjuk,
                  >>  ahol egy db egyperces magyar videó van,
                  >>  a felesleges letöltögetések elkerülése miatt)
                >> és elmenti a videó szövegét a video_Keyword.txt-be

ytKeyword       >> megkérdezi hogy milyen szót keresel
                >> és ellenőrzi a lementett szövegekben,
                >> hogy található-e ilyen.


--------
-- TELEPÍTÉS --
------

> API KEY:
ytScrapper5 >> Google Cloud projekt / YouTube Data API v3 certification key

> PIP INSTALL:
python
googleapiclient
langdetect 
whisper
yt_dlp

> PATH:
ffmpeg



 --------
-- TODO -- 
  ------

Projekt:        API számlázás

Scrapper:       napi dátomozású mentés
                darabszám növelés

SpeechToText:   video_Scrapper.txt szétbontása
                helyes mappa / fájlnév mentés

Keyword:        több kulcsszós keresés

Projekt:        web integrálás


------------------------------------------------


> Bp. 2025.05.28.

Ecsedi Tamás József

> ecsitomi


