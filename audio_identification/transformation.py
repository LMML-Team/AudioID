import numpy as np
import matplotlib.mlab as mlab

def print_spectrogram(samples, fs=44100):
    S, freqs, times = mlab.specgram(samples, NFFT=4096, Fs=fs,
                                    window=mlab.window_hanning,
                                    noverlap=(4096 // 2))
    return np.array([S, freqs, times])

