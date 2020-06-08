#blaine county talk radio
from playsound import playsound; 
import random, os;

def run():
    station_dir = "./audio_files/BLAINE COUNTY TALK RADIO/";
    #master lists
    mono_solo_ml = os.listdir(station_dir + "mono_solo/"); #['MONO_BLESS_YOUR_HEART.wav', 'MONO_ZBEYOND_INSEMINATION_PART_2.wav', 'MONO_BCR_COMMUNITY_HOUR.wav', 'MONO_BEYOND_INSEMINATION.wav'];
    id_ml = os.listdir(station_dir + "id/"); #['ID_09.wav', 'ID_06.wav', 'ID_10.wav', 'ID_02.wav', 'ID_04.wav', 'ID_01.wav', 'ID_05.wav', 'ID_11.wav', 'ID_08.wav', 'ID_03.wav', 'ID_07.wav'];
    
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

 
