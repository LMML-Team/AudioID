from .peak_find import peak_find


def song_fp(samples, prnt_spectro=False):
    """
    Takes samples from songs, uses peaks to calculate fingerprints

    Parameters
    -----------
    samples: song sample data. Used in peak_find()
        ndarray of song sample data
    prnt_spectro: boolean (default = False)
        whether a spectrogram of the song should be shown on screen

    Return
    -------
    fingerprints: A set of tuples containing (f1, f2, dt).
        gives relationships between frequencies and times of concurrent peaks in song data
    """

    t, f = peak_find(samples, prnt_spectro)

    fingerprints = set()
    for n, t1 in enumerate(t) :
        for j, t2 in enumerate(t[min(n + 1, len(t) - 1) : min(n + 20, len(t))]) :
            if n + j + 1 < len(t) :
                fingerprints.add((f[n], f[n + j + 1], t2 - t1))

    return frozenset(fingerprints)
