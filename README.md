# GTA V  Radio
GTA V radio stand alone program

![example image](https://github.com/yobleck/gtav_radio/blob/master/images/example1.png)

## WIP

Frontend:
  - python 
    - ncurses (Linux)
    - window-curses (windows)

Backend:
  - [playsound](https://github.com/TaylorSMarks/playsound)
    - Linux:[gstreamer](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c)
    - win:windll.winmm

## OS Versions:
  ### Functioning:
    - Linux beta
    - windows 7 beta
  ### WIP:
    Linux polishing up
    Windows 7 (which will hopefully work with 8-10 as well)
  ### Maybe Coming:
    Android through termux app?
   - [termux play audio](https://github.com/termux/play-audio/) looks promising
  ### Probably NOT Happening:
    MacOS, iOS
    website, electron webapp

## Installation:
  - Download from here
  - make sure python 3.8 or later is installed
  - if on windows type 'pip install windows-curses' in terminal
  - download gstreamer if on linux
  - audio files to be ripped from game or downloaded from 3rd party and placed in audio_files folder where gtav_radio.py is located
    - audio files not included here for legal reasons
    - aHR0cHM6Ly9tZWdhLm56L2ZpbGUvckpNSGdZclQjLUtyOEJKbkV1NGd6cXh6YUdVUnRSNF96RlNWMTctY1hWRWNYNHhCTFNJTQ==
  - To run open terminal and type cd "file/path/to/gtav_radio-master"
  - Then type python gtav_radio.py
  
  - self radio songs are placed in ./audio_files/SELF RADIO/songs
  - these instructions assume some basic familiarity with the command line.
  - (standalone version with no dependencies to come)
    
 ## Controls
  - "esc" to quit program
  - "q" to stop station
  - "i/w/up" and "k/s/down" to navigate stations
  - "enter" to play station
  - "/" help menu
  - "m" mode switch (full radio / no ads or news WIP / music only
  
  ## TODO
  - radio station transition sound effect when switching between two stations
