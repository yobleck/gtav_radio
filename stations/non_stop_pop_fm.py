#non stop pop fm
from playsound import playsound; 
import random, os;

def run():
    station_dir = "./audio_files/NON STOP POP FM/";
    #master lists
    song_ml = os.listdir(station_dir + "songs/"); #['SOMETHING_GOT_ME_STARTED_REMIX.wav', 'THE_TIME_IS_NOW.wav', 'ALRIGHT.wav', 'TAPE_LOOP.wav', 'TAPE_LOOP_ALT.wav', 'GIMME_MORE.wav', 'SCANDALOUS.wav', 'ADULT_EDUCATION.wav', 'WAIT.wav', 'TENNIS_COURT.wav', 'ONLY_GIRL_IN_THE_WORLD.wav', 'MEET_ME_HALFWAY.wav', 'MOVES_LIKE_JAGGER.wav', 'PURE_SHORES.wav', 'WEST_END_GIRLS.wav', 'PROMISES_PROMISES.wav', 'WORK.wav', 'DONT_WANNA_FALL_IN_LOVE.wav', 'DAYS_GO_BY.wav', 'LIVING_IN_A_BOX.wav', 'SIX_UNDERGROUND.wav', 'LADY_HEAR_ME_TONIGHT.wav', 'KIDS.wav', 'ON_OUR_OWN.wav', 'WITH_EVERY_HEARTBEAT.wav', 'FEEL_GOOD_INC.wav', 'APPLAUSE.wav', 'MIDNIGHT_CITY.wav', 'ONE_THING.wav', 'LETS_GO_ALL_THE_WAY.wav', 'I_WANT_IT_THAT_WAY.wav', 'MUSIC_SOUNDS_BETTER_WITH_YOU.wav', 'ANTHEM.wav', 'TELL_TO_MY_HEART.wav', 'ME_AND_YOU.wav', 'GLAMOROUS.wav', 'BAD_GIRLS.wav', 'RYTHM_OF_THE_NIGHT.wav', 'SMALLTOWN_BOY.wav', 'EVERYTHING_SHE_WANTS.wav', 'COOLER_THAN_ME.wav', 'SEND_ME_AN_ANGEL.wav', 'NEW_SENSATION.wav'];
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
