#radio mirror park
from playsound import playsound; 
import random, os;

def run():
    station_dir = "./audio_files/RADIO MIRROR PARK/";
    #master lists
    song_ml = os.listdir(station_dir + "songs/"); #['DARK_MATTER.wav', 'HEART_IN_THE_PIPES.wav', 'HEARTBREAK.wav', 'NOWHERE_TO_GO.wav', 'WHEN_YOURE_OUT.wav', 'THE_SET_UP.wav', 'TRULY_ALIVE.wav', 'DO_YOU_BELIEVE.wav', 'HOLD_ON_HOLY_GHOST.wav', 'STRANGERS_IN_THE_WIND.wav', 'HIGH_PRESSURE.wav', 'FORGET.wav', 'SLEEPWALKING.wav', 'OLD_LOVE.wav', 'CRYSTALFILM.wav', 'ONE_GIRL_ONE_BOY.wav', 'LITTLE_WHITE_LIE.wav', 'IN_REAL_LIFE.wav', 'PSYCHIC_CITY.wav', 'SHOOTING_HOLES.wav', 'JASMINE.wav', 'SHINE_A_LIGHT.wav', 'SO_MANY_DETAILS.wav', 'MESMERIZED.wav', 'DONT_COME_CLOSE.wav', 'COLOURS.wav', 'POLISH_GIRL.wav', 'FLUTES.wav', 'SOMETIMES.wav', 'NEW_BEAT.wav', 'PHARAOHS.wav', 'CHANGE_OF_COAST.wav', 'FEEL_THE_SAME.wav', 'LIVING_IN_AMERICA.wav', 'LUCKY_BOY.wav', 'THE_DRUMMER.wav', 'BOOGIE_IN_ZERO_GRAVITY.wav', 'ALWAYS.wav', 'O_N_E.wav', 'FROM_NOWHERE.wav'];
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
 
