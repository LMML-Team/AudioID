import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import librosa

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

from microphone import record_audio
from microphone import play_audio

song_data = {}


def new_song(song_path, sf=44100) :
    '''Adds new song to database with song_name as key
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
                          -song_path[::-1].find(".") - 1] if "/" in song_path else song_pathsong_path[: -song_path[::-1].find(".") - 1]
    if song_name not in song_data :
        samples, sf = librosa.load(song_path, sr=sf)
        song_data[song_name] = (samples, sf, song_path)


def record_song(time=10) :
    '''Records song and converts samples from bits to python integers

    Parameters
    -------------
    time: int
        length of time to record audio (default = 10)

    Return
    -------------
    samples: np.array, dtype = np.int16
        array of audio samples as integers
    '''
    byte_encoded_signal, sr = record_audio(time)
    samples = np.hstack(tuple(np.fromstring(i, dtype=np.int16) for i in byte_encoded_signal))
    return samples


def list_songs():
    """Returns the list of song names as a np.array"""
    return song_data.keys()
