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

    t, f = peak_find(samples)

    fingerprints = set()
    for n, t1 in enumerate(t) :
        for j, t2 in t[min(n + 1, len(indices[0] - 1) : min(n + 20, len(indices[0]))] :
            fingerprints.add((f[n], f[n + j + 1], t2 - t1))

    return frozenset(fingerprints)
