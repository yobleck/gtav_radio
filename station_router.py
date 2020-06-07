#this is stupid but I couldn't think of another way to call different files in a compact manner
from stations import (test_station, los_santos_rock_radio, vinewood_boulevard_radio, channel_x, non_stop_pop_fm, west_coast_talk_radio_95_6, 
                      space_103_2, radio_mirror_park, radio_los_santos, rebel_radio, soulwax_fm, east_los_fm, west_coast_classics,
                      blaine_county_talk_radio,the_blue_ark, worldwide_fm, flylo_fm, the_low_down_91_1, self_radio, blonded_los_santos_97_8_fm,
                      the_lab, Ifruit_radio);

#TODO: pass through CWD so statin files can have absolute file path
def route(station_number):
    
    if(station_number not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22]): #temp until all stations are in
        station_number = -1;
    
    if(station_number == -1):
        test_station.run();
    
    if(station_number == 1):
        los_santos_rock_radio.run();

    if(station_number == 2):
        non_stop_pop_fm.run();

    if(station_number == 3):
        radio_los_santos.run();

    if(station_number == 4):
        channel_x.run();

    if(station_number == 5):
        west_coast_talk_radio_95_6.run();

    if(station_number == 6):
        rebel_radio.run();

    if(station_number == 7):
        soulwax_fm.run();

    if(station_number == 8):
        east_los_fm.run();

    if(station_number == 9):
        west_coast_classics.run();

    if(station_number == 10):
        blaine_county_talk_radio.run();

    if(station_number == 11):
        the_blue_ark.run();
        pass; 
    if(station_number == 12):
        worldwide_fm.run();

    if(station_number == 13):
        flylo_fm.run();

    if(station_number == 14):
        the_low_down_91_1.run();

    if(station_number == 15):
        radio_mirror_park.run();

    if(station_number == 16):
        space_103_2.run();

    if(station_number == 17):
        vinewood_boulevard_radio.run();

    if(station_number == 18):
        the_lab.run();

    if(station_number == 19):
        blonded_los_santos_97_8_fm.run();

    if(station_number == 20):
        pass; 
    if(station_number == 21):
        Ifruit_radio.run();
        pass; 
    if(station_number == 22):
        self_radio.run();


if __name__ == "__route__":
    route();
