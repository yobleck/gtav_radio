#main file
#runs curses for ui and user input and spawns threads for the actual radio
import curses, os;
from curses import panel;
import multiprocessing;
import station_router;
import radio_settings;
import time, math;

#various helper functions
def create_thread(input_station): #allows calling the same thread over and over
    temp = multiprocessing.Process(target=station_router.route, args=(input_station,));
    temp.daemon = True;
    return temp;

def kill_audio(thread):
    thread.kill(); #kill child
    thread.join(); #re-kill zombie child
    return False;

def draw_logo(input_station_list, input_window): #TODO: use getmaxyx to automatically pick file size. images might need formatting
    if(input_window.getmaxyx()[0] < 40):           #or use braile characters with SET_LOCALE LC_ALL
        logo_file = open("./images/30/" + input_station_list, "r").readlines();
    elif(input_window.getmaxyx()[0] < 80):
        logo_file = open("./images/40/" + input_station_list, "r").readlines();
    elif(input_window.getmaxyx()[0] < 100):
        logo_file = open("./images/80/" + input_station_list, "r").readlines();
    else:
        logo_file = open("./images/100/" + input_station_list, "r").readlines();
    input_window.erase();
    input_window.box();
    for y in range(0, len(logo_file)):
        input_window.addstr(y+1,1,logo_file[y][:-1]);
    input_window.refresh();
    
def cleanup_now_playing(input_window): #TODO:replace with write_to_now_playing.py
    f = open("./stations/now_playing.txt","w"); #resets now playing file when program closes
    f.write("Now Playing: Welcome to GTA V Radio");
    f.close();
    input_window.refresh();


#main function obviously
def main(stdscr):
    #curses initializers
    curses.use_default_colors();
    curses.curs_set(0);
    term_h, term_w = stdscr.getmaxyx();
    if(term_w < 50 or term_h < 25):
        raise Exception("Window size is too small");
    
    #other initializers
    station_list = ["LOS SANTOS ROCK RADIO", "NON STOP POP FM", "RADIO LOS SANTOS", "CHANNEL X", "WEST COAST TALK RADIO 95.6", "REBEL RADIO", "SOULWAX FM", "EAST LOS FM", "WEST COAST CLASSICS", "BLAINE COUNTY TALK RADIO", "THE BLUE ARK", "WORLDWIDE FM", "FLYLO FM", "THE LOW DOWN 91.1", "RADIO MIRROR PARK", "SPACE 103.2", "VINEWOOD BOULEVARD RADIO", "THE LAB", "BLONDED LOS SANTOS 97.8 FM", "LOS SANTOS UNDERGROUND RADIO", "iFRUIT RADIO", "SELF RADIO"];
    current_station = None; #read from settings.ini and auto play if not None and autoplay is True
    highlighted_station = 1; #should be 0 but seee qqqqqqqq issue
    running = True;
    is_playing = False;
    
    #displays logo
    logo_scr = curses.newwin(term_h-2,term_w-34,0,0); #(height, width, start_y, start_x)  #old width: math.floor(term_w/2)
    logo_scr.box();
    #draw_logo(station_list[0], 20, logo_scr); # TODO: draw logo for autoplay
    logo_scr.refresh();
    
    #displays list of stations
    main_menu_scr = curses.newwin(math.floor(term_h)-1,34,0,term_w-34); #34 old width and start_x: math.floor(term_w/2)
    main_menu_scr.box();
    for x in range(1,len(station_list)+1):
        main_menu_scr.addnstr(x,1,station_list[x-1],main_menu_scr.getmaxyx()[1]-2);
    main_menu_scr.chgat(highlighted_station,1,len(station_list[highlighted_station-1]),curses.A_REVERSE);
    main_menu_scr.refresh();
    main_menu_in_focus = True;
    
    #now playing screen
    now_playing_scr = curses.newwin(1,math.floor(3*term_w/4),term_h-1,0);
    f = open("./stations/now_playing.txt","r");
    now_playing_scr.addnstr(f.readline(),now_playing_scr.getmaxyx()[1]);
    f.close();
    now_playing_scr.refresh();
    now_playing_counter = 0;
    
    #mode screen
    mode = radio_settings.get_setting("mode=");
    mode_scr = curses.newwin(1,math.floor(term_w/4),term_h-1,math.floor(3*term_w/4));
    mode_scr.addnstr("Mode: " + mode, mode_scr.getmaxyx()[1]);
    mode_scr.refresh();
    
    #displays settings menu
    settings_scr = curses.newwin(term_h,term_w,0,0); 
    settings_scr.addstr("SETTINGS, HELP AND INFORMATION\n"); #will crash if terminal is tiny
    settings_scr.addstr("\"/\" for this menu\n");
    settings_scr.addstr("\"esc\" to quit program\n");
    settings_scr.addstr("\"i\" and \"k\" to navigate stations\n");
    settings_scr.addstr("\"enter\" to select station\n");
    settings_scr.addstr("\"q\" to stop station\n");
    settings_scr.addstr("\"m\" to toggle full_radio/music_only/no_ads_news mode\n");
    settings_scr.addstr("\t Station must be restarted to take effect\n");
    settings_scr.addstr("Created by yobleck: https:/www.github.com/yobleck/gtav_radio\n");
    settings_scr.addstr("All artworks are copyright of Rockstar\n");
    settings_scr.addstr("All songs copyright of their respective owners\n");
    settings_scr.addstr("Copyrighted files are not included with this program\n");
    settings_visible = False;
    
    test_scr = curses.newwin(1,math.floor(term_w/2),term_h-2,0);
    test_scr.nodelay(True); #allows loop to run without waiting for input
    test_scr.addstr("/ for help"); #TODO: remove when done testing logo sizes
    
    #main do stuff loop
    while(running):
        x = test_scr.getch(); #get user input
        if(x != -1):
            test_scr.clear();
            test_scr.addstr(str(x));
            test_scr.refresh();
        
        if(x == 27): #kill while loop and exit program with "esc"
            running = False;
        
        if(x == 49 and not is_playing): #play audio test with "1"
            audio_thread = create_thread(-1);
            audio_thread.start();
            is_playing = True;
            
        if(x == 10 and current_station != highlighted_station and main_menu_in_focus): #enter key to start playing station
            if("audio_thread" in locals()): #kill current thread
                kill_audio(audio_thread);
                if(isinstance(current_station,int)):
                    main_menu_scr.addstr(current_station,len(station_list[current_station-1])+2,"   "); #remove current station arrow
            current_station = highlighted_station; #get highlight number and set current station
            #call play to specific station
            audio_thread = create_thread(station_list[current_station-1]); #TODO:replace with current_station once station code is ready
            audio_thread.start();
            is_playing = True;
            draw_logo(station_list[current_station-1], logo_scr);
            main_menu_scr.addstr(current_station,len(station_list[current_station-1])+2,"<--"); #points at current station when highlight moves
            main_menu_scr.refresh();
            test_scr.addstr("s" + str(current_station));
            
        
        #kill audio with "q"
        if(x == 113 and "audio_thread" in locals()): 
            is_playing = kill_audio(audio_thread);
            cleanup_now_playing(now_playing_scr);
            logo_scr.clear(); # get rid of logo
            logo_scr.box();
            logo_scr.refresh();
            if(isinstance(current_station,int)):
                main_menu_scr.addstr(current_station,len(station_list[current_station-1])+2,"   "); #maybe put these in cleanup_now_playing
                main_menu_scr.refresh();
        try: #kill audio_thread after it finishes    move closer to top of loop?
            if(audio_thread.is_alive() == False):
                is_playing = kill_audio(audio_thread); #murder zombie child to prevent horde
                current_station = None;
                cleanup_now_playing(now_playing_scr);
        except:
            pass;
        
        
        
        #main menu navigation
        if(x in [107,115] and main_menu_in_focus): # k key down
            if(highlighted_station < 22): #main_menu_scr.getmaxyx()[0]-4): #keep inbounds TODO: rework this to account for varying heights
                main_menu_scr.chgat(highlighted_station,1,len(station_list[highlighted_station-1]),curses.A_NORMAL); #un-highlight
                highlighted_station += 1;
                main_menu_scr.chgat(highlighted_station,1,len(station_list[highlighted_station-1]),curses.A_REVERSE); #highlight
                main_menu_scr.refresh();
        if(x in [105,119] and main_menu_in_focus): # i key up
            if(highlighted_station > 1):
                main_menu_scr.chgat(highlighted_station,1,len(station_list[highlighted_station-1]),curses.A_NORMAL);
                highlighted_station -= 1;
                main_menu_scr.chgat(highlighted_station,1,len(station_list[highlighted_station-1]),curses.A_REVERSE);
                main_menu_scr.refresh();
                
        
        if(x in [47,63]): # /? key for settings. actual editing or just for show?
            if(settings_visible == False):
                settings_scr.redrawwin();
                settings_scr.refresh();
                settings_visible = True;
                main_menu_in_focus = False;
            else:
                logo_scr.redrawwin();
                logo_scr.refresh();
                main_menu_scr.redrawwin();      #wrap all this stuff up in a function
                main_menu_scr.refresh();
                test_scr.redrawwin();
                test_scr.refresh();
                now_playing_scr.redrawwin();
                now_playing_scr.refresh();
                mode_scr.redrawwin();
                mode_scr.refresh();
                settings_visible = False;
                main_menu_in_focus = True;
                
        
        if(x == 109): # m key for mode toggling
            if(mode == "music_only"):
                radio_settings.set_setting("mode=", "no_ads_news");
                mode = "no_ads_news";
            elif(mode == "no_ads_news"):
                radio_settings.set_setting("mode=", "full_radio");
                mode = "full_radio";
            elif(mode == "full_radio"):
                radio_settings.set_setting("mode=", "music_only");
                mode = "music_only";
            mode_scr.clear();
            mode_scr.addnstr("Mode: " + mode, mode_scr.getmaxyx()[1]);
            mode_scr.refresh();
        
        
        #read file to get now playing. jank workaround cause I couldn't be bothered to learn multiprocessing.Value
        now_playing_counter += 1;
        if(now_playing_counter % 100 == 0 and main_menu_in_focus): #massive number to avoid unnecessary file IO. see sleep
            now_playing_counter = 0;
            f = open("./stations/now_playing.txt","r");
            now_playing_scr.clear();
            now_playing_scr.addnstr(0,0,f.readline(),now_playing_scr.getmaxyx()[1]);
            f.close();
            now_playing_scr.refresh();
        
        time.sleep(.01); #this is to try and reduce cpu usage. more testing needed
#####end while loop
    cleanup_now_playing(now_playing_scr);


#run! returns terminal to sane state if program crashes
if __name__ == "__main__":
    if(os.name == "nt"): #mandatory for windows
        multiprocessing.freeze_support();
    curses.wrapper(main); 
