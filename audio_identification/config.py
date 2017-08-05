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
    global song_data
    song_data = tuple(list(x for x in song_data if x[1] != song_name))
    save()


def remove_album(album_name) :
    '''
    Removes specified album's songs from database with song_name as key

    Parameters
    -------------
    album_name: song_object.key
        string with album's name
    '''
    global song_data
    song_data = tuple(list(x for x in song_data if x[2] != album_name))
    save()


def remove_artist(artist_name) :
    '''
    Removes specified artist's songs from database with song_name as key

    Parameters
    -------------
    artist_name: song_object.key
        string with artist's name
    '''
    global song_data
    song_data = tuple(list(x for x in song_data if x[3] != artist_name))
    save()


def clear_database() :
    '''
    Clears database of song fingerprints
    '''
    global song_data
    song_data = ()
    save()


def list_songs() :
    '''
    Returns the list of song names as a np.array
    '''
    unzipped = list(zip(*song_data))
    zipped = list(zip(*unzipped[1:]))
    return zipped


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
    num_matches = len(best_match[0] & fingerprint)
    print(num_matches)

    if num_matches >= 80:
        str_match = "Strong match"
    elif num_matches >= 50:
        str_match ="Good match"
    elif num_matches >= 25:
        str_match = "Weak match"
    else:
        str_match = "No match"

    # add functionality to check if song is good match (based on number of matches)
    return best_match[1:], str_match
