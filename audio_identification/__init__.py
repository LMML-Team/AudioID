import numpy as np
import librosa
import eyed3

from microphone import record_audio
# from microphone import play_audio

from .config import *
from .fingerprinting import song_fp
from .graph_spectrogram import print_spectro


def record_song(time=10, prnt_spectro=False) :
    """
    Records song and converts samples from bits to python integers

    Parameters
    -----------
    time: int
        length of time to record audio (default = 10)
    prnt_spectro: boolean (default = False)
        whether a spectrogram of the song should be shown on screen

    Return
    -------
    best_match: str
        name of song best matching recorded audio
    """
    byte_encoded_signal, sr = record_audio(time)
    samples = np.hstack(tuple(np.fromstring(i, dtype=np.int16) for i in byte_encoded_signal))

    fingerprint = song_fp(samples, prnt_spectro)
    best_match, str_match = match_song(fingerprint)

    song_name, album, singer = best_match
    return song_name, album, singer, str_match



def import_song_file(song_path, sf=44100) :
    """
    Adds new song to database

    Parameters
    -----------
    song_path: r"PATH"
        string with song's path
    sf: int > 0
        sampling frequency of song (default = 44100)

    Return
    -------
    sample: np.array
        array of song samples
    """
    song_name = eyed3.load(song_path).tag.title
    song_album = eyed3.load(song_path).tag.album
    song_artist = eyed3.load(song_path).tag.artist

    if (song_name, song_album, song_artist) not in list_songs() :
        samples, sf = librosa.load(song_path, sr=sf)
        fingerprint = song_fp(samples)
        new_song(fingerprint, song_name, song_album, song_artist)

        save()
    else :
        raise Exception("Song is already in database")
