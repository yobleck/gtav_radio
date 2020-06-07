#the blue ark
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/THE BLUE ARK/";
    
    #master lists
    song_ml = ['NIGHT_NURSE.wav', 'CRAZY_GIRL.wav', 'DISCO_DEVIL.wav', 'ODD_RAS.wav', 'ADDI_TRUTH.wav', 'GRUMBLIN_DUB.wav', 'GUN_SHOT_A_FIRE.wav', 'CHAPTER3.wav', 'KINGSTON_BE_WISE.wav', 'NOBODY_MOVE_GET_HURT.wav', 'PSYCHO.wav', 'MONEY_IN_MY_POCKET.wav', 'WE_NEVER_FEAR_DEM.wav', 'ROAST_FISH_AND_CORNBREAD.wav', 'I_AM_A_MADMAN.wav', 'SONS_OF_SLAVES.wav', 'TOPIC_OF_THE_DAY.wav', 'LOYALS.wav', 'MR_MONEY_MAN.wav', 'MONEY_COME_MONEY_GO.wav', 'KINGSTON_TOWN.wav'];
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
 
