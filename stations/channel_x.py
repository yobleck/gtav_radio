#channel x
from playsound import playsound; 
import random;

def run(cwd):
    station_dir = cwd + "/audio_files/CHANNEL X/";
    
    #master lists
    song_ml = ['PERVERT.wav', 'LIFE_OF_CRIME.wav', 'SILENT_MAJORITY.wav', 'DONT_PUSH_ME_AROUND.wav', 'WHATS_NEXT.wav', 'DONT_NEED_SOCIETY.wav', 'LINDA_BLAIR.wav', 'AMOEBA.wav', 'JOHN_WAYNE.wav', 'THE_ENEMY.wav', 'MY_WAR.wav', 'THE_MOUTH_DONT_STOP.wav', 'BLOWN_AWAY.wav', 'BORED_OF_YOU.wav', 'ROCK_HOUSE.wav', 'LEXICON_DEVIL.wav', 'LOS_ANGELES.wav', 'SUBLIMINAL.wav'];
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
