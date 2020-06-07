#radio los santos
from playsound import playsound; 
import random;

def run():
    station_dir = "./audio_files/RADIO LOS SANTOS/";
    #master lists
    song_ml = ['HUNNID_STAX.wav', 'LIFE_OF_A_MACK.wav', 'ALI_BOMAYE.wav', 'HOLD_UP.wav', 'HOW_IT_WAS.wav', 'BASSHEADS.wav', 'UPPER_ECHELON.wav', 'SWIMMING_POOLS.wav', 'SLOW_DOWN.wav', 'DO_IT_BIG.wav', 'IM_A_REAL_ONE.wav', 'R_CALI.wav', 'WORK_YOUNG_SCOOTER.wav', 'MILLIONS.wav', 'SELLIN_DOPE.wav', 'SAY_THAT_THEN.wav', 'WORK_FERG.wav', 'STILL_LIVIN.wav', 'HOOD_GONE_LOVE_IT.wav', 'ILLUMINATE.wav', 'ADHD.wav', 'I_CANT_WAIT_SCOOTER.wav', 'COLLARD_GREENS.wav', 'TOO_HOOD.wav', 'EVERYDAY.wav', 'SMOKIN_AND_RIDIN.wav', 'BUGATTI.wav', 'EASILY.wav', 'RELAXIN.wav', 'BAD_NEWS.wav', 'KUSH_COMA.wav'];
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
        num = random.randint(0,len(temp_song_list)-1);
        f = open("./stations/now_playing.txt","w");
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "songs/" + temp_song_list[num]);
        temp_song_list.pop(num);
    
if __name__ == "__run__":
    run();
 
