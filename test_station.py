#test station
from playsound import playsound;

def play(file):
    playsound(file, True); 

def run():
    #master lists
    song_ml = ["/home/yobleck/gtav_radio/misc/vote_or_else.mp3"];
    dj_ml = [];
    ad_ml = [];

    play(song_ml[0]);
    
if __name__ == "__run__":
    run();
