#curated stations with no ads
#usually only a few large files
#blonded, east los, flylo, soulwax, the lab, worldwide
from playsound import playsound;
from random import choice;
from write_to_now_playing import write_to_now_playing;
import os;

def play(input_station): #ignore modes once implemented
    #get files
    source_dir = "./audio_files/" + input_station + "/songs/";
    songs_ml = os.listdir(source_dir);
    
    temp_songs = list(songs_ml);
    
    playing = True;
    while(playing):
        rand_song = choice(temp_songs);
        
        write_to_now_playing(rand_song);
        playsound(source_dir + rand_song);
        temp_songs.remove(rand_song);
        
        if(not temp_songs):
            temp_songs = list(songs_ml);
        
#windows if name main
