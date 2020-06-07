#blonded los santos 97.8 fm
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/BLONDED LOS SANTOS 97.8 FM/";
    
    #master lists
    song_ml = ['RADIO_XM17_P3.wav', 'RADIO_XM17_P1.wav', 'RADIO_XM17_P2.wav'];
    
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

