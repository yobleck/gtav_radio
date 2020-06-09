def write_to_now_playing(playing_file):
    f = open("./stations/now_playing.txt","w");
    f.write("Now Playing: " + playing_file);
    f.close(); 
