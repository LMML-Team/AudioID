def convert_frequencies(samples):
    '''Given samples from a song, this function will convert
    the samples into an array of frequencies

    Parameters
    -------------
    N/A

    Return
    -------------
    N/A
    '''
    coefs = np.fft.rfft(samples)  # Array of coefficients for frequencies
    length = len(data) / 44100  # Total duration of the song
    k = np.arange(len(coefs)) / length  # Frequencies
    return [coefs, length, k]

def make_spectrogram()