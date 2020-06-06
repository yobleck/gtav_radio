#import os, sys, inspect;
#cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"stations")))
#if cmd_subfolder not in sys.path:
    #sys.path.insert(0, cmd_subfolder)
from stations import test_station, los_santos_rock_radio, vinewood_boulevard_radio, channel_x, non_stop_pop_fm, west_coast_talk_radio_95_6;

#this is stupid but I couldn't think of another way to call different files in a compact manner

def route(station_number):
    if(station_number not in [1,2,4,5,17]): #temp until all stations are in
        station_number = -1;
    
    if(station_number == -1):
        test_station.run();
    if(station_number == 1):
        los_santos_rock_radio.run();
        pass;
    if(station_number == 2):
        non_stop_pop_fm.run();
        pass; 
    if(station_number == 3):
        pass; 
    if(station_number == 4):
        channel_x.run();
        pass; 
    if(station_number == 5):
        west_coast_talk_radio_95_6.run();
        pass; 
    if(station_number == 6):
        pass; 
    if(station_number == 7):
        pass; 
    if(station_number == 8):
        pass; 
    if(station_number == 9):
        pass; 
    if(station_number == 10):
        pass; 
    if(station_number == 11):
        pass; 
    if(station_number == 12):
        pass; 
    if(station_number == 13):
        pass; 
    if(station_number == 14):
        pass; 
    if(station_number == 15):
        pass; 
    if(station_number == 16):
        pass; 
    if(station_number == 17):
        vinewood_boulevard_radio.run();
        pass; 
    if(station_number == 18):
        pass; 
    if(station_number == 19):
        pass; 
    if(station_number == 20):
        pass; 
    if(station_number == 21):
        pass; 
    if(station_number == 22):
        pass; 

if __name__ == "__route__":
    route();
