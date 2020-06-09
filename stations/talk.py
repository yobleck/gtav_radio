#talk radio stations
from playsound import playsound;
from random import choice;
from write_to_now_playing import write_to_now_playing;
import os;

def play(input_station): #ignore modes once implemented
    source_dir = None;
    #master lists. these should neve change once populated
    id_ml = [];
    mono_solo_ml = [];
    
    #check which talk station to play
    if(input_station == "BLAINE COUNTY TALK RADIO"):
        source_dir = "./audio_files/" + input_station + "/";
        id_ml = os.listdir(source_dir + "id/");
        mono_solo_ml = os.listdir(source_dir + "mono_solo/");
        
    if(input_station == "WEST COAST TALK RADIO 95.6"):
        source_dir = "./audio_files/" + input_station + "/";
        id_ml = os.listdir(source_dir + "/id/");
        mono_solo_ml = os.listdir(source_dir + "mono_solo/");
    
    temp_id = id_ml;
    temp_mono_solo = mono_solo_ml;
    
    playing = True; #TODO: pause feature
    while(playing):
        #get random files from list
        rand_id = choice(temp_id);
        rand_mono_solo = choice(temp_mono_solo);
        temp_id.remove(rand_id);
        
        playsound(source_dir + "id/" + rand_id); #play station id
        write_to_now_playing(rand_mono_solo); #write file to play in now playing file
        playsound(source_dir + "mono_solo/" + rand_mono_solo); #play main file
        temp_mono_solo.remove(rand_mono_solo); #remove from temp list to stop duplicates
        
        #repopulate temp lists when empty
        if(not temp_id):
            temp_id = id_ml;
        if(not temp_mono_solo):
            temp_mono_solo = mono_solo_ml;
            
#if __name__ == "__play__": #needed for windows?
    #play();
