#rebel radio
from playsound import playsound; 
import random;

def run(cwd):
    station_dir = cwd + "/audio_files/REBEL RADIO/";
    #master lists
    song_ml = ['IF_WANT_TO_GET_HEAVEN.wav', 'YOU_TOOK_ALL_THE_RAMBLIN_OUT.wav', 'CANT_HARDLY_STAND.wav', 'HIGHWAY_MAN.wav', 'IT_DONT_HURT_ANYMORE.wav', 'WHISKEY_RIVER.wav', 'GET_OUTTA_MY_CAR.wav', 'GET_WITH_IT.wav', 'SHE_MADE_TOOTHPICKS_OUT_OF_ME.wav', 'THE_GENERAL_LEE.wav', 'I_AINT_LIVING_LONG_LIKE_THIS.wav', 'DIPPIN_SNUFF.wav', 'DIVORCE.wav', 'ARE_YOU_SURE_HANK.wav', 'CRAZY_ARMS.wav', 'CONVOY.wav', 'IT_WONT_BE_LONG_HATING_YOU.wav'];
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
 
