import numpy as np
from.spectrogram import make_spectrogram


def peak_find(samples):
    """
    Finds peak values of given sample data
    
    Parameter(s)
    -------------
    samples: song sample data for peaks to be found in.

    Returns
    -------------
    Boolean np.ndarray with true values at peaks, false values at non-peaks

    """
    spectro_output = make_spectrogram(samples)
    s = spectro_output['spectro']

    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, 20)

    ys, xs = np.histogram(s.flatten(), bins=len(freqs) // 2, normed=True)
    dx = xs[-1] - xs[-2]
    cdf = np.cumsum(ys) * dx
    cutoff = xs[np.searchsorted(cdf, 0.77)]

    foreground = (s >= cutoff)

    output = np.logical_and(S == foreground, S == maximum_filter(S, neighborhood)).T
    return {'indices': list(zip(np.where(output))), 'f': spectro_output['f'], 't': spectro_output['t']}
