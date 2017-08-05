"""Hello - need to update this description."""

import numpy as np
import librosa
import eyed3

from microphone import record_audio
# from microphone import play_audio

from .config import *
from .fingerprinting import song_fp


def record_song(time=10) :
    '''Records song and converts samples from bits to python integers

    Parameters
    -------------
    time: int
        length of time to record audio (default = 10)

    Return
    -------------
    best_match: str
        name of song best matching recorded audio
    '''
    byte_encoded_signal, sr = record_audio(time)
    samples = np.hstack(tuple(np.fromstring(i, dtype=np.int16) for i in byte_encoded_signal))

    fingerprint = song_fp(samples)
    best_match, str_match = match_song(fingerprint)

    #return "{} by {} from {} is detected as a {}".format(best_match[0], best_match[1], best_match[2], str_match)
    song_name, album, singer = best_match
    return song_name, album, singer, str_match



def import_song_file(song_path, sf=44100) :
    '''
    Adds new song to database with song_name as key
    and tuple of samples, sampling rate,
    (fingerprint dictionary -- to be implemented) and song_path as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    sf: int > 0
        sampling frequency of song (default = 44100)

    Return
    -------------
    sample: np.array
        array of song samples
    '''
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
