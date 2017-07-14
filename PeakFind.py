def peak_find(S):
    """
    Parameter(s)
    ---------------------------
    S: np.ndarray for spectrogram of 2-Dimensions. One dimension is time bins, one is frequency bins. Contains integer values representing amplitude.

    Returns
    ---------------------------
    Boolean np.ndarray with true values at peaks, false values at non-peaks

    """

    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, 20)

    ys, xs = np.histogram(S.flatten(), bins=len(freqs) // 2, normed=True)
    dx = xs[-1] - xs[-2]
    cdf = np.cumsum(ys) * dx
    cutoff = xs[np.searchsorted(cdf, 0.77)]

    foreground = (S >= cutoff)

    return np.logical_and(data == foreground, data == maximum_filter(data, neighborhood))