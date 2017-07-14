import numpy as np
import matplotlib.mlab as mlab

def make_spectrogram(samples, fs=44100):
    '''
    Takes the samples from songs and converts them to a spectrogram

    Parameters
    -------------
    samples: np.array
        samples from a given song, in array form
    fs: int
        sampling rate of the samples

    Returns
    -------------
    data: np.array
        returns:
            S:     the spectrogram, a 2D array of |c_k| values. Axis-0 (row) is the frequency, axis-1 (col) is the time
            freqs: an array of frequency values, which allows you to correspond the axis-0 bins to actual frequencies
            times: an array of timevalues, which allows you to correspond the axis-1 bins to actual times
    '''

    S, freqs, times = mlab.specgram(samples, NFFT=4096, Fs=fs,
                                    window=mlab.window_hanning,
                                    noverlap=(4096 // 2))
    data = np.array([S, freqs, times])
    return data