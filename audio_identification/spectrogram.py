import numpy as np
import matplotlib.mlab as mlab


def make_spectrogram(samples, fs=44100):
    """
    Takes the samples from songs and converts them to a spectrogram

    Parameters
    -------------
    samples: np.array
        samples from a given song, in 1D array form
    fs: int
        sampling rate of the samples

    Returns
    -------------
    spectro: np.array
        the spectrogram, a 2D array of |c_k| values. Axis-0 (row) is the frequency, axis-1 (col) is the time
    freqs:   np.array
        1D array of frequency values, which allows you to correspond the axis-0 bins to actual frequencies
    times:   np.array
        1D array of time values, which allows you to correspond the axis-1 bins to actual times
    """

    spectro, freqs, times = mlab.specgram(samples, NFFT=4096, Fs=fs,
                                          window=mlab.window_hanning,
                                          noverlap=(4096 // 2))
    return {'spectro': spectro, 'f': freqs, 't': times}
