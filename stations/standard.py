#standard file for most radio stations
#includes full_radio, no_ads_news, music_only
#channel x, los santos rock, non stop pop, radio los santos, mirror park, rebel radio, space, blue ark, lowdown, vinewood, west coast classics
from playsound import playsound;
from random import choice, random;
from write_to_now_playing import write_to_now_playing;
import os;

def branching(input_list, input_dir, input_type):
    rand = choice(input_list);
    write_to_now_playing(rand);
    input_list.remove(rand);
    playsound(input_dir + input_type + rand);
    return rand;
    
####################

def __play_radio(input_station): #TODO: read if ads_news or no from settings.ini
    station_dir =  "./audio_files/" + input_station + "/";
    
    #master lists and temp lists
    temp_songs = songs_ml = os.listdir(station_dir + "songs/");
    temp_mono_solo = mono_solo_ml = os.listdir(station_dir + "mono_solo/");
    temp_intro = intro_ml = os.listdir(station_dir + "intro/");
    temp_general = general_ml = os.listdir(station_dir + "general/");
    temp_id = id_ml = os.listdir(station_dir + "id/");
    temp_time = time_ml = os.listdir(station_dir + "time/");
    temp_to = to_ml = os.listdir(station_dir + "to/");
    temp_ad = ad_ml = os.listdir("./audio_files/RADIO_ADVERTS/");
    temp_news = news_ml = os.listdir("./audio_files/RADIO_NEWS/");
    
    type_list = ["songs/", "mono_solo/", "intro/", "general/", "id/", "time/", "to/", ""];
    next_song = None;
    
    playing = True;
    while(playing):
        if(next_song): #play song dictated by intro at bottom of loop
            playsound(station_dir + "songs/" + str([i for i in temp_songs if next_song in i][0])); #search for specific song based on substring
            next_song = None;
            #TODO: not removing song from list may result in it playing twice too close together
        else: #or play random song
            branching(temp_songs, station_dir, type_list[0]);
            if(not temp_songs): #these are for repopulating empty lists
                temp_songs = songs_ml;
        
        rng = random();
        if(rng > 0.5): #play another song
            pass;
        else:
            if(rng < 0.5 and rng > 0.375): #play mono_solo
                branching(temp_mono_solo, station_dir, type_list[1]);
                if(not temp_mono_solo):
                    temp_mono_solo = mono_solo_ml;
            
            if(rng < 0.375 and rng > 0.25): #play general
                branching(temp_general, station_dir, type_list[3]);
                if(not temp_general):
                    temp_general = general_ml;
            
            if(rng < 0.25 and rng > 0.125): #play time
                branching(temp_time, station_dir, type_list[5]);
                if(not temp_time):
                    temp_time = time_ml;
            
            if(rng < 0.125 and rng > 0.0): # play ads or news
                to_what = branching(temp_to, station_dir, type_list[6]);
                if("AD" in to_what):
                    branching(temp_ad, "./audio_files/RADIO_ADVERTS/", type_list[7]);
                if("NEWS" in to_what):
                    branching(temp_news, "./audio_files/RADIO_NEWS/", type_list[7]);
                if(not temp_ad):
                    temp_ad = ad_ml;
                if(not temp_news):
                    temp_news = news_ml;
            
            branching(temp_id, station_dir, type_list[4]); #play id
            if(not temp_id):
                temp_id = id_ml;
            
            next_song = branching(temp_intro, station_dir, type_list[2])[:-7]; #play intro and return next song
            if(not temp_intro):                                                # by clipping _01.wav off intro
                temp_intro = intro_ml;
        

####################

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
    
    
####################

def play(input_station): #TODO: implement modes later
    __play_radio(input_station);


#windows if name = main thing?
