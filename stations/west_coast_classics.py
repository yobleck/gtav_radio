#west coast classics
from playsound import playsound; 
import random;

def run():
    station_dir =  "./audio_files/WEST COAST CLASSICS/";
    
    #master lists
    song_ml = ['WE_ROLL_DEEP.wav', 'FIRST_OF_THE_MONTH.wav', 'BOW_DOWN.wav', 'SERVIN_EM_HEAT.wav', 'WHAT_YOU_WANNA_DO.wav', 'THE_NEXT_EPISODE.wav', 'STILL_D_R_E.wav', 'NOTHIN_BUT_THE_CAVI_HIT.wav', 'AFRO_PUFFS.wav', 'AMBITIONZ_AZ_A_RIDAH.wav', 'C_WALK.wav', 'BALLAD_OF_A_MENACE.wav', 'THE_MURDA_SHOW.wav', 'APPETITE_FOR_DESTRUCTION.wav', 'STRAIGHT_UP_MENACE.wav', 'THIS_DJ.wav', 'WHAT_WOULD_YOU_DO.wav', 'LIKE_A_PIANO.wav', 'CAPTAIN_SAVE_A_HOE.wav', 'LATE_NIGHT_HYPE.wav', 'SHERM_STICK.wav', 'DOLLAZ_AND_SENSE.wav', 'NO_MORE_QUESTIONS.wav', 'YOU_KNOW_HOW_WE_DO.wav', 'MIND_PLAYING_TRICKS.wav', 'I_GOT_FIVE_ON_IT.wav', 'GANGSTA_GANGSTA.wav', 'GIN_AND_JUICE.wav', 'SO_YOU_WANT_TO_BE_A_GANGSTER.wav'];
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
