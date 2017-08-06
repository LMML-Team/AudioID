from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure

import numpy as np
from .spectrogram import make_spectrogram


def peak_find(samples, prnt_spectro=False):
    '''
    Finds peak values of given sample data

    Parameters
    -----------
    samples: ndarray
        song sample data for peaks to be found in
    prnt_spectro: boolean (default = False)
        whether a spectrogram of the song should be shown on screen

    Returns
    --------
    times: ndarray
        indices of peak times
    freqs: ndarray
        indices of peak frequencies
    '''
    s, f, t = make_spectrogram(samples, prnt_spectro)

    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, 20)

    ys, xs = np.histogram(s.flatten(), bins=len(f) * len(t) // 2, normed=True)
    dx = xs[-1] - xs[-2]
    cdf = np.cumsum(ys) * dx
    cutoff = xs[np.searchsorted(cdf, 0.77)]

    output = np.logical_and(s >= cutoff, s == maximum_filter(s, footprint=neighborhood)).T
    tf = np.where(output)
    return tf[0], tf[1]
