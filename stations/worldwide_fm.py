#worldwide fm
from playsound import playsound; 
import random, os;

def run():
    station_dir =  "./audio_files/WORLDWIDE FM/";
    
    #master lists
    wwfm_ml = os.listdir(station_dir + "wwfm/"); #['0x15ED4708.wav', '0x04A02233.wav', '0x1E4AFD9D.wav', '0x1EDECB2F.wav'];
    
    temp_song_list = wwfm_ml;
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1); #rng
        f = open("./stations/now_playing.txt","w"); #for now playing
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "wwfm/" + temp_song_list[num]); #play song
        temp_song_list.pop(num); #remove from list so only plays once
        
        
    
if __name__ == "__run__":
    run(); 
 
 
