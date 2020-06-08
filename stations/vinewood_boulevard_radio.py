#vinewood boulevard radio
from playsound import playsound; 
import random, os;

def run():
    station_dir = "./audio_files/VINEWOOD BOULEVARD RADIO/";
    #master lists
    song_ml = os.listdir(station_dir + "songs/"); #['FIRE_DOESNT_BURN_ITSELF.wav', 'DIDDY_WAH_DIDDY.wav', 'COCAINE.wav', 'CALIFORNIA_GIRLS.wav', 'TURN_IT_AROUND.wav', 'CRAWLING_AFTER_YOU.wav', 'NINE_IS_GOD.wav', 'SLEEPWALKER.wav', 'USED_BLOOD.wav', 'THIS_MYSTIC_DECADE.wav', 'BLACK_GREASE.wav', 'THE_DREAM.wav', 'ANSWER_TO_YOURSELF.wav', 'SIXPACK.wav', 'FALL_IN_LINE.wav', 'WET_BLANKET.wav', 'NEXT_STOP.wav', 'WHO_NEEDS_YOU.wav', 'GONE_FOR_GOOD.wav', 'HYSTERIA.wav'];
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
