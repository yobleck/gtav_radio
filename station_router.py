#this is stupid but I couldn't think of another way to call different files in a compact manner
from stations import (test_station, self_radio, Ifruit_radio, talk, curated, standard);
#TODO: just pass through string grom gtav_radio.station_list rather that have all these if statements
#TODO: reduce if statements down to standard, curated, talk oddballs
def route(station_number, debug = False):
    
    if(not debug):
        if(station_number in ["WEST COAST TALK RADIO 95.6","BLAINE COUNTY TALK RADIO"]):
            talk.play(station_number);
        elif(station_number in ["SOULWAX FM","EAST LOS FM","WORLDWIDE FM","FLYLO FM","THE LAB","BLONDED LOS SANTOS 97.8 FM"]):
            curated.play(station_number);
        elif(station_number in ["LOS SANTOS UNDERGROUND RADIO", -1]):
            test_station.run();
        elif(station_number == "SELF RADIO"):
            self_radio.run();
        elif(station_number == "iFRUIT RADIO"):
            Ifruit_radio.run();
        else:
            standard.play(station_number);
    
    else: #this is so I don't have to type out the station name during testing. type number and True
        if(station_number == -1):
            test_station.run();
        
        if(station_number == 1):
            standard.play("LOS SANTOS ROCK RADIO");

        if(station_number == 2):
            standard.play("NON STOP POP FM");

        if(station_number == 3):
            standard.play("RADIO LOS SANTOS");

        if(station_number == 4):
            standard.play("CHANNEL X");

        if(station_number == 5):
            talk.play("WEST COAST TALK RADIO 95.6");

        if(station_number == 6):
            standard.play("REBEL RADIO");

        if(station_number == 7):
            curated.play("SOULWAX FM");

        if(station_number == 8):
            curated.play("EAST LOS FM");

        if(station_number == 9):
            standard.play("WEST COAST CLASSICS");

        if(station_number == 10):
            talk.play("BLAINE COUNTY TALK RADIO");

        if(station_number == 11):
            standard.play("THE BLUE ARK");
        
        if(station_number == 12):
            curated.play("WORLDWIDE FM");

        if(station_number == 13):
            curated.play("FLYLO FM");

        if(station_number == 14):
            #the_low_down_91_1.run();
            standard.play("THE LOW DOWN 91.1");

        if(station_number == 15):
            standard.play("RADIO MIRROR PARK");

        if(station_number == 16):
            standard.play("SPACE 103.2");

        if(station_number == 17):
            standard.play("VINEWOOD BOULEVARD RADIO");

        if(station_number == 18):
            curated.play("THE LAB");

        if(station_number == 19):
            curated.play("BLONDED LOS SANTOS 97.8 FM");

        if(station_number == 20): #couldn't find files for los santos underground radio
            test_station.run();
            
        if(station_number == 21):
            Ifruit_radio.run();
        
        if(station_number == 22):
            self_radio.run();


if __name__ == "__route__": #for windows?
    route();
