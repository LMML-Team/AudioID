import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def convert_frequencies(samples):
    '''Given samples from a song, this function will convert
    the samples into an array of frequencies

    Parameters
    -------------
    N/A

    Return
    -------------
    N/A
    '''
    coefs = np.fft.rfft(samples)  # Array of coefficients for frequencies
    length = len(data) / 44100  # Total duration of the song
    k = np.arange(len(coefs)) / length  # Frequencies
    return [coefs, length, k]

def print_spectrogram(samples, fs=44100):
    S, freqs, times = mlab.specgram(samples, NFFT=4096, Fs=fs,
                                    window=mlab.window_hanning,
                                    noverlap=(4096 // 2))
    return np.array(S, freqs, times)

