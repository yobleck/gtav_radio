#Ifruit radio
#from playsound import playsound; 
import random, os, subprocess;

def run():
    station_dir =  "./audio_files/iFRUIT RADIO/";
    
    #master lists
    song_ml = os.listdir(station_dir + "songs/"); #['BACK_TO_BASICS_FLOATING_POINTS_REMIX.wav', 'PATTERN_CHANEL.wav', 'ACT_UP.wav', 'KNOCK_YOUR_BLOCK_OFF.wav', 'WINGS.wav', 'MONEY_IN_THE_BANK.wav', 'ALIENS.wav', 'KILLIN_DEM.wav', 'BOP.wav', 'HUNDRED_K_ON_A_COUPE.wav', 'NUMB_NUMB_JUICE.wav', 'TBD.wav', 'WITH_THE_THING.wav', 'DANCE_IN_THE_WATER.wav', 'OPOTOYI.wav', 'GREAZE_MODE.wav', 'I_NEED.wav', 'HIGHEST_IN_THE_ROOM.wav', 'HOT_REMIX.wav', 'POP_STAR.wav', 'KISS_AND_TELL.wav', 'ORIGINAL_FORMAT.wav', 'W.wav', 'CASH_SHIT.wav', 'CRIME_PAYS.wav', 'EVERYTHING_SHE_WANTS.wav', 'KITCHEN_KINGS.wav', 'MUST_BE.wav'];
    mono_solo_ml = os.listdir(station_dir + "mono_solo/");
    intro_ml = os.listdir(station_dir + "intro/");
    id_ml = os.listdir(station_dir + "id/");
    time_ml = os.listdir(station_dir + "time/");
    
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
 
