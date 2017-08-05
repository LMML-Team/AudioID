import numpy as np
import matplotlib.pyplot as plt


def print_spectro(spectro, freqs, times):
    """
    Prints out the input spectrogram

    Parameter
    ----------------
    spectro_results: dictionary (len=3)
        1: 2D array of Ck values, axis-0 is frequency, axis-1 is time
        2: 1D array of frequencies
        3: 1D array of times

    """
    fig, ax = plt.subplots()
    ax.set_yscale(freqs)
    ax.set_xscale(times)
    plt.imshow(spectro)
