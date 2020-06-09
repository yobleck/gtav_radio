#standard file for most radio stations
#includes full_radio, no_ads_news, music_only
#channel x, los santos rock, non stop pop, radio los santos, mirror park, rebel radio, space, blue ark, lowdown, vinewood, west coast classics
from playsound import playsound;
from random import choice;
from write_to_now_playing import write_to_now_playing;
import os;

def __play_radio(input_station): #TODO: this entire thing
    station_dir =  "./audio_files/" + input_station + "/";
    
    #master lists
    songs_ml = os.listdir(station_dir + "songs/");
    mono_solo_ml = os.listdir(station_dir + "songs/");
    intro_ml = os.listdir(station_dir + "intro/");
    general_ml = os.listdir(station_dir + "general/");
    id_ml = os.listdir(station_dir + "id/");
    time_ml = os.listdir(station_dir + "time/");
    to_ml = os.listdir(station_dir + "to/");
    ad_ml = os.listdir("./audio_files/RADIO_ADVERTS/");
    news_ml = os.listdir("./audio_files/RADIO_NEWS/");

##########

def __play_music_only(input_station):
    station_dir =  "./audio_files/" + input_station + "/";
    songs_ml = os.listdir(station_dir + "songs/");
    
    temp_songs = songs_ml;
    playing = True;
    while(playing):
        rand_song = choice(temp_songs);
        write_to_now_playing(rand_song)
        playsound(station_dir + "songs/" + rand_song);
        temp_songs.remove(rand_song);
        
        if(not temp_songs):
            temp_songs = songs_ml
    
    
##########

def play(input_station): #implement modes later
    __play_music_only(input_station);


#windows if name = main thing?
