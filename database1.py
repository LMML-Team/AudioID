import os

# song_read = open('database.txt', 'r')


def new_song(song_path, sf=44100) :
    '''
    Saves song to a .txt file
    Adds new song to database with song_name as key
    and tuple of samples, sampling rate,
    (fingerprint dictionary -- to be implemented) and song_path as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    sf: int > 0
        sampling frequency of song (default = 44100)
    Returns
    --------------
    N/A
    '''
    song_write = open('database.txt', 'w')
    song_name = song_path[-song_path[::-1].find("/") :
                          -song_path[::-1].find(".") - 1] if "/" in song_path else song_pathsong_path[: -song_path[::-1].find(".") - 1]
    string ="\""+ song_name + "\" ::: " # + function of the finger printing
    song_write.append(string)
    
    song_write.close()
    
    # the data for a song before fourier transformation
    song_data = {}
    if song_name not in song_data :
        samples, sf = librosa.load(song_path, sr=sf)
        song_data[song_name] = (samples, sf, song_path)

def remove_song(song_name):
    """
    Removes specified song from 
    
    Parameters
    --------------
    song_name: the name of the song
    
    Returns
    --------------
    N/A
    """
    song_write = open('database.txt', 'w')
    song_close()

def load():
    """
    Removes specified song from 
    
    Parameters
    --------------
    song_name: the name of the song
    
    Returns
    --------------
    N/A
    """
    pass

def list_songs():
    """
    Returns the list of songs as a np.array
    
    Parameters
    --------------
    N/A
    
    Returns
    --------------
    np.array: the list of song names
    """
    song_names = []
    return song_names
