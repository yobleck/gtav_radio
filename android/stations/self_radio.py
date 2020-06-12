#self radio
#from playsound import playsound; 
import random, os, subprocess;

def run():
    station_dir =  "./audio_files/SELF RADIO/";
    
    #master lists
    song_ml = os.listdir(station_dir + "songs/");
    mono_solo_ml = os.listdir(station_dir + "solo/");
    intro_ml = os.listdir(station_dir + "intro/");
    outro_ml = os.listdir(station_dir + "outro/");
    id_ml = os.listdir(station_dir + "id/");
    time_ml = os.listdir(station_dir + "time/");
    to_ml = os.listdir(station_dir + "to/");
    ad_ml = ["./audio_files/RADIO_ADVERTS/"];
    news_ml = ["./audio_files/RADIO_NEWS/"];
    
    temp_song_list = list(song_ml);
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1); #rng
        #f = open("./stations/now_playing.txt","w"); #for now playing
        #f.write("Now Playing: " + str(temp_song_list[num]));
        #f.close();
        #playsound(station_dir + "songs/" + temp_song_list[num]); #play song
        subprocess.run(["play-audio", station_dir + "songs/" + temp_song_list[num]]);
        temp_song_list.pop(num); #remove from list so only plays once
        if(not temp_song_list):
            temp_song_list = list(song_ml);
        
        
    
if __name__ == "__run__":
    run(); 
 
