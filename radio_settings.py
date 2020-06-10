#provides functions for extracting values form settings.ini

import re;

def get_mode():
    try: #I made this fucked up one liner for fun. I'll probably never remember how it works. Good luck future me.
        mode = [j for j in ["music_only","full_radio","no_ads_news"] if j in re.search("mode=(.+?)\\n",[i for i in open("./settings.ini","r").readlines() if "mode=" in i][0]).group(1)][0];
    except:
        raise Exception("Invalid mode in settings.ini \n make sure there is a setting called mode= \n with a value of full_radio , no_ads_news or music_only ");
    return mode;

def set_mode(input_mode):
    fr = open("./settings.ini", "r").readlines()
    for x in range(0,len(fr)):
        if("mode=" in fr[x]):
            fr[x] = "mode=" + input_mode + "\n";
            fw = open("./settings.ini", "w");
            fw.writelines(fr);
            fw.close();
    
