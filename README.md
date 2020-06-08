# GTA V  Radio
GTA V radio stand alone program

![example image](https://github.com/yobleck/gtav_radio/blob/master/images/example1.png)

## WIP

Frontend:
  - python 
    - ncurses (linux)
    - window-curses or unicurses for windows

Backend:
  - [playsound](https://github.com/TaylorSMarks/playsound)
    - linux:[gstreamer](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c)
    - win:windll.winmm

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
    - audio files not included here for legal reasons
    - aHR0cHM6Ly9tZWdhLm56L2ZpbGUvbkZkV2lBREwjd1lJcm4zSXloMEh6MTZUemNsNzVmd0EyT053NHVOMXZSVDh2c042dUxuOA==
  - (standalone version with no dependencies to come)
    
 ## Controls
  - "esc" to quit program
  - "q" to stop station
  - "i/w" and "k/s" to navigate stations (arrow keys currently cause crash)
  - "enter" to play station
  - "/" help menu
  - "m" mode switch (WIP)
