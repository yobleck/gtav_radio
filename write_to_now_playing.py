def write_to_now_playing(playing_file):
    from multiprocessing import shared_memory;
    now_playing_sm = shared_memory.SharedMemory(name="now_playing"); #access shared memory object
    now_playing_sm.buf[:now_playing_sm.size] = bytes([0] * now_playing_sm.size); #clear it
    now_playing_sm.buf[:len(playing_file)] = bytes(playing_file, "utf-8"); #write to it
    now_playing_sm.close();

