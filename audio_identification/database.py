import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import librosa
import pickle

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

from microphone import record_audio
from microphone import play_audio

import fingerprinting as fp

#TODO: complete remove_song(song_name)

song_data = {}


def save() :
    '''
    Saves song_data to a .pickle file
    '''
    with open('song_data.pickle', 'wb') as f:
        pickle.dump(song_data, f, pickle.HIGHEST_PROTOCOL)


def load() :
    '''
    Loads .pickle file and makes it to be readable in this syntax
    '''
    with open('song_data.pickle', 'rb') as f:
        song_data = pickle.load(f)


def new_song(song_path, sf=44100) :
    '''
    Adds new song to database with song_name as key
    and tuple of samples, sampling rate,
    (fingerprint dictionary -- to be implemented) and song_path as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    sf: int > 0
        sampling frequency of song (default = 44100)
    '''
    song_name = song_path[-song_path[::-1].find("/") :
                          -song_path[::-1].find(".") - 1] if "/" in song_path else song_path[: -song_path[::-1].find(".") - 1]
    if song_name not in song_data :
        samples, sf = librosa.load(song_path, sr=sf)
        song_data[song_name] = (samples, sf, song_path)

def remove_song(song_name) :
    '''
    Removes specified song from database with song_name as key
    
    Parameters
    -------------
    song_name: song_object.key
        string with song's name
    '''
    # TODO: figure out how to remove certain info from the pickle file

def list_songs() :
    '''
    Returns the list of song names as a np.array
    '''
    return song_data.keys()
