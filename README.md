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

# Files in audio_identification
## Fingerprinting
Find the peaks using in the functions Peak_find.
Then use the function song_fp to return the fingerprints of the song (the unique characteristics of the song)
## Config
A file that takes care of the database of songs.
## Peak_find
## Song_data.pickle
## Spectrogram
