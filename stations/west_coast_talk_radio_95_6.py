#west coast talk radio 95.6
from playsound import playsound; 
import random;

def run(cwd):
    station_dir = cwd + "/audio_files/WEST COAST TALK RADIO 95.6/";
    #master lists
    mono_solo_ml = ['MONO_CHATTERSPHERE.wav', 'MONO_FERNANDO_SHOW_1.wav', 'MONO_DCHAKRA_ATTACK_PART_2.wav', 'MONO_CHAKRA_ATTACK_PART_1.wav'];
    intro_ml = ['ID_09.wav', 'ID_06.wav', 'ID_10.wav', 'ID_02.wav', 'ID_04.wav', 'ID_01.wav', 'ID_05.wav', 'ID_11.wav', 'ID_08.wav', 'ID_03.wav', 'ID_07.wav'];
    
    temp_song_list = mono_solo_ml;
    while(temp_song_list):
        num = random.randint(0,len(temp_song_list)-1);
        f = open("./stations/now_playing.txt","w");
        f.write("Now Playing: " + str(temp_song_list[num]));
        f.close();
        playsound(station_dir + "mono_solo/" + temp_song_list[num]);
        temp_song_list.pop(num);
    
if __name__ == "__run__":
    run();

