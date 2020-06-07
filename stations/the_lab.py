 #the lab
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/THE LAB/";
    
    #master lists
    song_ml = ['LAB_P1.wav','LAB_P2.wav'];
    
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


