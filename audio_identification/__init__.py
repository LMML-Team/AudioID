"""Hello - need to update this description."""

import numpy as np
import librosa

from microphone import record_audio
# from microphone import play_audio

from .database import _load
from .database import _save
from .database import song_data
from .database import new_song
from .database import match_song
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
    if not song_data:
        _load()
    byte_encoded_signal, sr = record_audio(time)
    samples = np.hstack(tuple(np.fromstring(i, dtype=np.int16) for i in byte_encoded_signal))

    fingerprint = song_fp(samples)
    best_match = match_song(fingerprint)

    return best_match


def import_file(song_path, sf=44100) :
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
    if not song_data:
        _load()
    song_name = song_path[-song_path[::-1].find("/") : -song_path[::-1].find(".") - 1] if "/" in song_path else song_path[: -song_path[::-1].find(".") - 1]
    if song_name not in song_data :
        samples, sf = librosa.load(song_path, sr=sf)

    fingerprint = song_fp(samples)
    new_song(song_name, fingerprint)

    _save()
