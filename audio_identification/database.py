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

#TODO: complete remove_song(song_name)


song_data = {}


def _load() :
    '''
    Loads .pickle file and makes it to be readable in this syntax
    '''
    with open('song_data.pickle', 'rb') as f:
        song_data = pickle.load(f)


def _save() :
    '''
    Saves song_data to a .pickle file
    '''
    with open('song_data.pickle', 'wb') as f:
        pickle.dump(song_data, f, pickle.HIGHEST_PROTOCOL)


def new_song(song_name, fingerprint) :
    '''
    Adds new song to database with song_name as key
    fingerprint as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    fingerprint: ---------
        ----------------------
    '''
    song_data[fingerprint] = song_name


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


def match_song(fingerprint) :
    '''
    Returns name of song with highest number of matches to specified fingerprint

    Parameters
    -------------
    fingerprint: set of tuples
        the song-to-be-identified's fingerprint

    Return
    -------------
    song_name: str
        name of song with best match
    '''
    matches = 0
    best_match = set{}
    for fp in iter(song_data) :
        if len(fp & fingerprint) > matches :
            matches = len(fp & fingerprint)
            best_match = fp

    # add functionality to check if song is good match (based on number of matches)
    return song_data[best_match]
