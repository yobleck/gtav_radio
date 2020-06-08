#space 103.2
from playsound import playsound; 
import random, os;

def run():
    station_dir = "./audio_files/SPACE 103.2/";
    #master lists
    song_ml = os.listdir(station_dir + "songs/"); #['PARTY_ALL_THE_TIME.wav', 'BACK_AND_FORTH.wav', 'FLASHLIGHT.wav', 'FUNKASIZE_YOU.wav', 'CANT_HOLD_BACK.wav', 'TONIGHT.wav', 'FLASHBACK.wav', 'YOURE_THE_ONE_FOR_ME.wav', 'JOYSTICK.wav', 'HEARTBREAKER.wav', 'HEART_BEAT.wav', 'GOTTA_GET_MY_HANDS_ON_SOME_MONEY.wav', 'CUTIE_PIE.wav', 'ID_RATHER_BE_WITH_YOU.wav', 'DO_IT_ROGER.wav', 'HABOGLABOTRIBIN.wav', 'SKELETONS.wav', 'IM_IN_LOVE.wav', 'WALKING_INTO_SUNSHINE.wav', 'NIGHTS_FEEL_LIKE.wav', 'GIVE_IT_TO_ME_BABY.wav', 'MOTHERSHIP_CONNECTION.wav'];
    mono_solo_ml = os.listdir(station_dir + "mono_solo/");
    intro_ml = os.listdir(station_dir + "intro/");
    general_ml = os.listdir(station_dir + "general/");
    id_ml = os.listdir(station_dir + "id/");
    time_ml = os.listdir(station_dir + "time/");
    to_ml = os.listdir(station_dir + "to/");
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
