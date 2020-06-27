#provides functions for extracting values form settings.ini

import re;

def get_setting(input_str): #TODO: rename this to get_valueof(input) and have if statements change j in list values. with input being mode, autoplay etc.
    try: #I made this fucked up one liner for fun. I'll probably never remember how it works. Good luck future me.
        mode = [j for j in ["music_only","full_radio","no_ads_news"] if j in re.search(input_str + "(.+?)\\n",[i for i in open("./settings.ini","r").readlines() if input_str in i][0]).group(1)][0];
    except:
        raise Exception("Invalid mode in settings.ini \n make sure there is a setting called mode= \n with a value of full_radio , no_ads_news or music_only ");
    return mode;

def set_setting(input_setting, input_str):
    fr = open("./settings.ini", "r").readlines()
    for x in range(0,len(fr)):
        if(input_setting in fr[x]):
            fr[x] = input_setting + input_str + "\n";
            fw = open("./settings.ini", "w");
            fw.writelines(fr);
            fw.close();
    
#mode = [j for j in ["music_only","full_radio","no_ads_news"] if j in re.search("mode=(.+?)\\n",[i for i in open("./settings.ini","r").readlines() if "mode=" in i][0]).group(1)][0];
#                                                                      4.regex to get value                 1.open file               2.put lines in list1
#                                                                                                                                                   3.check if mode in list1 and return el 0
#                     6. check if list2 contains above                                                                                                                 5.return list2
#                                                                                                                                                                                7.return final value
