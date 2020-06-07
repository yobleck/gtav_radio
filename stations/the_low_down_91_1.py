 #the low down 91.1
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/THE LOW DOWN 91.1/";
    
    #master lists
    song_ml = ['CLIMAX.wav', 'BOUNCY_LADY.wav', 'O_O_H_CHILD.wav', 'I_BELIEVE_IN_MIRACLES.wav', 'MAGIC_MOUNTAIN.wav', 'SMILING_FACES.wav', 'FUNNY_FEELING.wav', 'READY_OR_NOT.wav', 'CHANGIN.wav', 'CRUISIN.wav', 'CALIFORNIA_SOUL.wav', 'VIVA_TIRADO.wav', 'ASHLEYS_ROACHCLIP.wav', 'DO_IT_TIL_YOURE_SATISFIED.wav', 'SUPERMAN_LOVER.wav', 'STORIES.wav', 'I_GET_LIFTED.wav', 'THE_CISCO_KID.wav', 'HERCULES.wav', 'RUBBER_BAND.wav'];
    mono_solo_ml = [];
    intro_ml = [];
    general_ml = [];
    station_id = [];
    time_ml = [];
    to_ml = [];
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

