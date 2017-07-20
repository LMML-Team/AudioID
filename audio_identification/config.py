import pickle
import os.path

song_data = tuple()

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "song_data.pickle"), 'rb') as f:
    song_data = pickle.load(f)


def save() :
    '''
    Saves song_data to a .pickle file
    '''
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "song_data.pickle"), 'wb') as f:
        pickle.dump(song_data, f, pickle.HIGHEST_PROTOCOL)


def new_song(fingerprint, song_name, song_album, song_artist) :
    '''
    Adds new song to database with song_name as key
    fingerprint as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    fingerprint: ---------
        ----------------------
    '''
    global song_data
    song_data += ((fingerprint, song_name, song_album, song_artist),)

def remove_song(song_name) :
    '''
    Removes specified song from database with song_name as key

    Parameters
    -------------
    song_name: song_object.key
        string with song's name
    '''
    # TODO: figure out how to remove certain info from the pickle file


def list_songs() :
    '''
    Returns the list of song names as a np.array
    '''
    return song_data[:][1:]


def match_song(fingerprint) :
    '''
    Returns name of song with highest number of matches to specified fingerprint

    Parameters
    -------------
    fingerprint: set of tuples
        the song-to-be-identified's fingerprint

    Return
    -------------
    song_name: str
        name of song with best match
    '''
    best_match = max(song_data, key=lambda x: len(x[0] & fingerprint))
    # add functionality to check if song is good match (based on number of matches)
    return best_match[1:]
