# GTA V  Radio
GTA V radio stand alone program

## WIP

Frontend:
python ncurses 

Backend:
[playsound](https://github.com/TaylorSMarks/playsound)
  linux:[gstreamer](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c)
  win:windll.winmm

## OS Versions:
  ### Functioning:
    early linux beta
  ### WIP:
    linux more features
  ### Coming:
    Windows 7 (which will hopefully work with 8-10 as well)
    Android through termux app?
  ### Probably not happening:
    MacOS, iOS
    website, electron webapp

## Installation:
  - Download from here
  - make sure python 3.8 or later is installed
  - type 'pip install playsound' in terminal
  - download gstreamer if on linux
  - files to be downloaded from 3rd party and placed in audio_files folder where gtav_radio.py is located
    audio files not included here for legal reasons
    
 ## Controls
  - "esc" to quit program
  - "q" to stop station
  - "i" and "k" to navigate stations
  - "enter" to play station
  - "/" help menu
  - "m" mode switch (WIP)
