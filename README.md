_____________________________________
-------------------------------------
|| __ .. ** SAJTÓFIGYELŐ  ** .. __ ||
 -----------------------------------


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

ytScrapper5     >> listáz 5 db ma megjelent magyar YT videót
                >> a video_Scrapper.txt fájlba

ytSpeechToText  >> a demoban 1 videót .mp3-ba letölt
                >> a video_textToSpeech.txt-ből 
                >> (ez csak minta fájl a video_Scrapper.txt helyett)
                >> és elmenti video_Keyword.txt-be a szöveget

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


