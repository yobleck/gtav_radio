#los santos rock radio
from playsound import playsound; 
import random;

def run():
    station_dir = "/home/yobleck/gtav_radio/audio_files/LOS SANTOS ROCK RADIO/";
    #master lists
    song_ml = ['HEARTBEAT.wav', 'I_DONT_CARE_ANYMORE.wav', 'BLACK_VELVET.wav', 'BIG_LOG.wav', 'CATS_IN_THE_CRADLE.wav', 'I_WOULDNT_WANT_TO_BE.wav', 'THIRTY_DAYS_IN_THE_HOLE.wav', 'MISSISSIPPI_QUEEN.wav', 'HOLLYWOOD_NIGHTS.wav', 'FORTUNATE_SON.wav', 'RADIO_GA_GA.wav', 'SHADOWS_OF_THE_NIGHT.wav', 'ALL_THE_THINGS_SHE_SAID.wav', 'TOO_LATE_FOR_GOODBYES.wav', 'GIMME_ALL_YOUR_LOVIN.wav', 'BURNING_HEART.wav', 'LONELY_IS_THE_NIGHT.wav', 'ROUNDABOUT.wav', 'THE_BREAKUP_SONG.wav', 'I_CANT_WAIT.wav', 'RAIN.wav', 'CIRCLE_IN_THE_SAND.wav', 'BAKER_STREET.wav', 'PHOTOGRAPH.wav', 'SATURDAY_NIGHTS_ALRIGHT.wav', 'COMING_ON_STRONG.wav', 'HIGHER_LOVE.wav', 'IF_YOU_LEAVE_ME_NOW.wav', 'WE_BUILT_THIS_CITY.wav', 'WHAT_A_FOOL_BELIEVES.wav', 'ROCKIN_ME.wav', 'CARRY_ON_MY_WAYWARD_SUN.wav', 'DIRTY_WHITE_BOY.wav', 'PEACE_OF_MIND.wav', 'OGDENS_NUT_GONE_FLAKE.wav', 'NIGHT_MOVES.wav', 'IM_FREE.wav', 'DANGER_ZONE.wav'];
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
        num = random.randint(0,len(temp_song_list));
        playsound(station_dir + "songs/" + temp_song_list[num]);
        temp_song_list.pop(num);
    
if __name__ == "__run__":
    run();