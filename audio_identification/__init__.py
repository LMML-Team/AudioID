'''Hello - need to update this description'''

song_data = {}

def load() :
    '''
    Loads .pickle file and makes it to be readable in this syntax
    '''
    with open('song_data.pickle', 'rb') as f:
        song_data = pickle.load(f)
