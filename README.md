# AudioID
This is a student group project for MIT Beaver Works Summer Institute 2017: Cognitive Assistant Collaboration.

The project is designed to detect and record a sound from your designated microphone and identify the song that is playing based on the database.

# Setup
Install these packages and follow the instructions as stated: [Microphone](https://github.com/LLCogWorks2017/Microphone)

Clone this repository.
Open the folder of the cloned repository in Command Prompt.
Enter this command:
```shell
python setup.py develop
```

# Database
To import this package, there must be at least one song in the database (stored in song_data.pickle). The song_data.pickle file that comes with this package has a number of songs already stored; however if you wish to use your own music and delete the song_data.pickle file instead of using the clear_database function (as is the preferred method), to avoid any errors upon importing, comment out the following lines from the top of config.py:
```shell
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "song_data.pickle"), 'rb') as f:
    song_data = pickle.load(f)
```
