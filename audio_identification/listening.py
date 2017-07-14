import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import librosa

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

from microphone import record_audio
from microphone import play_audio


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
