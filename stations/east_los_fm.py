#east los fm
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/EAST LOS FM/";
    
    #master lists
    final_mix_ml = ["MEX_FINAL_MIX_32.wav"];
    
    
    temp_song_list = final_mix_ml;
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1); #rng
        f = open("./stations/now_playing.txt","w"); #for now playing
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "final_mix/" + temp_song_list[num]); #play song
        temp_song_list.pop(num); #remove from list so only plays once
        
        
    
if __name__ == "__run__":
    run(); 
 
 
