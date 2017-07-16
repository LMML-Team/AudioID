from .peak_find import peak_find


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
    indices = peaks['indices']
    frequencies = peaks['f']
    times = peaks['t']

    fingerprints = set()

    for n, ft1 in enumerate(zip(indices[0], indices[1])) :
        for f2, t2 in zip(indices[0][min(n + 1, len(indices[0] - 1)) : min(n + 20, len(indices[0]))], indices[1][min(n + 1, len(indices[1] - 1)) : min(n + 20, len(indices[1]))]) :
            fingerprints.add((ft1[0], f2, t2 - ft1[1]))

    return frozenset(fingerprints)
