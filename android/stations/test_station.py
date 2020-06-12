#test station
#from playsound import playsound;
import os, subprocess;

def run():
    #playsound("./misc/vote_or_else.mp3");
    subprocess.run(["play-audio","./misc/vote_or_else.mp3"]);
    
if __name__ == "__run__":
    run();
