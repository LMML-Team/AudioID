from .PeakFind import peak_find


def song_fp(samples):
    """
    Takes samples from songs, uses peaks to calculate fingerprints

    Parameters
    -------------
    samples: Song sample data. Used in peak_find()

    Return
    -------------
    fingerprints: A set of tuples containing (f1, f2, dt).
    Gives relationships between frequencies and times of concurrent peaks in song data

    """

    peaks = peak_find(samples)
    peak_indices = peaks['indices']
    frequencies = peaks['f']
    times = peaks['t']

    fingerprints = set()

    for n, f1, t1 in enumerate(peak_indices):
        for f2, t2 in peak_indices[n + 1: min(n + 20, len(peak_indices))]:
            fingerprints += (frequencies[f1], frequencies[f2], times[t2] - times[t1])

    return fingerprints
