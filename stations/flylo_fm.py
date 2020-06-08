#flylo fm
from playsound import playsound; 
import random, os;

def run():
    station_dir =  "./audio_files/FLYLO FM/";
    
    #master lists
    flylo_ml = os.listdir(station_dir + "flylo/"); #['0x08194D53.wav', '0x17E2800E.wav', '0x0339EC32.wav', '0x0A818E80.wav'];
    
    temp_song_list = flylo_ml;
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1); #rng
        f = open("./stations/now_playing.txt","w"); #for now playing
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "flylo/" + temp_song_list[num]); #play song
        temp_song_list.pop(num); #remove from list so only plays once
        
        
    
if __name__ == "__run__":
    run(); 
 
 
 
