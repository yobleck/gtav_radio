#self radio
from playsound import playsound; 
import random, os;

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
    ad_ml = [];
    news_ml = [];
    
    temp_song_list = song_ml;
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1); #rng
        f = open("./stations/now_playing.txt","w"); #for now playing
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "songs/" + temp_song_list[num]); #play song
        temp_song_list.pop(num); #remove from list so only plays once
        
        
    
if __name__ == "__run__":
    run(); 
 
