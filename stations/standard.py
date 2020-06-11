#standard file for most radio stations
#includes full_radio, no_ads_news, music_only
#channel x, los santos rock, non stop pop, radio los santos, mirror park, rebel radio, space, blue ark, lowdown, vinewood, west coast classics
from playsound import playsound;
from write_to_now_playing import write_to_now_playing;
import radio_settings;
from random import choice, random, randint;
import os, re;

def branching(input_list, input_dir, input_type):
    rand = choice(input_list);
    input_list.remove(rand);
    write_to_now_playing(rand);
    playsound(input_dir + input_type + rand); #comment this out to speed up debugging
    return rand;
    
####################

def __play_radio(input_station, mode):
    station_dir =  "./audio_files/" + input_station + "/";
    
    #master lists and temp lists
    songs_intro_ml = os.listdir(station_dir + "songs/");
    mono_solo_ml = os.listdir(station_dir + "mono_solo/");
    intro_ml = os.listdir(station_dir + "intro/");
    general_ml = os.listdir(station_dir + "general/");
    id_ml = os.listdir(station_dir + "id/");
    time_ml = os.listdir(station_dir + "time/");
    to_ml = os.listdir(station_dir + "to/");
    ad_ml = os.listdir("./audio_files/RADIO_ADVERTS/");
    news_ml = os.listdir("./audio_files/RADIO_NEWS/");
    
    songs_with_no_intro = 0;
    for song in songs_intro_ml: #this is for linking intro files to their respective songs so they stay in sync
        temp_list = [];
        for intro in intro_ml:
            if(song[:-4] in intro): #some songs may not have intro files
                temp_list.append(intro);
        songs_intro_ml[songs_intro_ml.index(song)] = [songs_intro_ml[songs_intro_ml.index(song)],temp_list];
        if(not temp_list):
            songs_with_no_intro += 1;
    
    temp_songs_intro = [];
    for x in range(0,len(songs_intro_ml)): #this is for transfering contents of the master list to the temp list
        temp_songs_intro.append(songs_intro_ml[x]);
    #print(temp_songs_intro);
    
    temp_mono_solo = list(mono_solo_ml); temp_general = list(general_ml); temp_id = list(id_ml); #this is same as above for all other lists
    temp_time = list(time_ml); temp_to = list(to_ml); temp_ad = list(ad_ml); temp_news = list(news_ml); 
    
    type_list = ["mono_solo/", "general/", "id/", "time/", "to/", ""]; #for passing folder structure to branching func
    next_song = None;
    
    
    playing = True;
    while(playing):
        if(next_song): #play song dictated by intro at bottom of loop
            #print("next_song", next_song); print("temp_songs_intro", temp_songs_intro, len(temp_songs_intro));
            temp_songs_intro.pop(rand_intro_index);
            write_to_now_playing(next_song);
            playsound(station_dir + "songs/" + next_song); #print("play specific song", next_song);
            next_song = None;
        else: #or play random song
            rand_song_index = randint(0,len(temp_songs_intro)-1);
            rand_song = temp_songs_intro[rand_song_index][0];
            temp_songs_intro.pop(rand_song_index);
            write_to_now_playing(rand_song);
            playsound(station_dir + "songs/" + rand_song); #print("play song", rand_song);
        
        #these are for repopulating empty lists
        if(len(temp_songs_intro) <= songs_with_no_intro): #repopulates songs_intro before is empty cause crash when rng<.5 and no songs with intro
            temp_songs_intro.clear();
            for x in range(0,len(songs_intro_ml)):
                temp_songs_intro.append(songs_intro_ml[x]);
        
        rng = random();
        if(rng > 0.5): #play another song
            pass;
        else:
            if(rng < 0.5 and rng > 0.375): #play mono_solo
                branching(temp_mono_solo, station_dir, type_list[0]);
                if(not temp_mono_solo):
                    temp_mono_solo = list(mono_solo_ml);
            
            if(rng < 0.375 and rng > 0.25): #play general
                branching(temp_general, station_dir, type_list[1]);
                if(not temp_general):
                    temp_general = list(general_ml);
            
            if(rng < 0.25 and rng > 0.125): #play time of day
                branching(temp_time, station_dir, type_list[3]);
                if(not temp_time):
                    temp_time = list(time_ml);
            
            if(rng < 0.125 and rng > 0.0 and mode == "full_radio"): # play ads or news
                to_what = branching(temp_to, station_dir, type_list[4]); #plays "to" ad or news
                if("AD" in to_what):
                    branching(temp_ad, "./audio_files/RADIO_ADVERTS/", type_list[5]); #plays actual ad
                if("NEWS" in to_what):
                    branching(temp_news, "./audio_files/RADIO_NEWS/", type_list[5]); #plays actual fake news
                if(not temp_to):
                    temp_to = list(to_ml);
                if(not temp_ad):
                    temp_ad = list(ad_ml);
                if(not temp_news):
                    temp_news = list(news_ml);
            if(rng < 0.125 and rng > 0.0 and mode == "no_ads_news"): # don't play ads or news
                pass;
            
            branching(temp_id, station_dir, type_list[2]); #play staion id
            if(not temp_id):
                temp_id = list(id_ml);
            
            while(True): #this is for making sure a song has an intro before attempting to play it
                rand_intro_index = randint(0,len(temp_songs_intro)-1);
                if(temp_songs_intro[rand_intro_index][1]):
                    rand_intro = choice(temp_songs_intro[rand_intro_index][1]);
                    break;
            write_to_now_playing(rand_intro);
            playsound(station_dir + "intro/" + rand_intro); #print("play intro", rand_intro);
            next_song = temp_songs_intro[rand_intro_index][0];
        
        #end of main loop
        

####################

def __play_music_only(input_station):
    station_dir =  "./audio_files/" + input_station + "/";
    songs_ml = os.listdir(station_dir + "songs/");
    
    temp_songs = list(songs_ml);
    playing = True;
    while(playing):
        rand_song = choice(temp_songs);
        write_to_now_playing(rand_song)
        playsound(station_dir + "songs/" + rand_song);
        temp_songs.remove(rand_song);
        
        if(not temp_songs):
            temp_songs = list(songs_ml);
    
    
####################

def play(input_station):
    mode = radio_settings.get_mode();
    if(mode == "music_only"):
        __play_music_only(input_station);
    else:
        __play_radio(input_station, mode);
    


#windows if name = main thing?
