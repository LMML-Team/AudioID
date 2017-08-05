from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure

import numpy as np
from .spectrogram import make_spectrogram


def peak_find(samples):
    '''
    Finds peak values of given sample data

    Parameter(s)
    -------------
    samples: song sample data for peaks to be found in.

    Returns
    -------------
    Boolean np.ndarray with true values at peaks, false values at non-peaks

    '''
    s, f, t = make_spectrogram(samples)
    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, 20)

    ys, xs = np.histogram(s.flatten(), bins=len(f * t) // 2, normed=True)
    dx = xs[-1] - xs[-2]
    cdf = np.cumsum(ys) * dx
    cutoff = xs[np.searchsorted(cdf, 0.77)]

    output = np.logical_and(s >= cutoff, s == maximum_filter(s, footprint=neighborhood)).T
    tf = np.where(output)
    return tf[0], tf[1]
