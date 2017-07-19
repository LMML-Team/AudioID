from distutils.core import setup
from setuptools import find_packages

try:
    import pyaudio
except ImportError:
    print("Warning: `pyaudio` must be installed in order to use `microphone`")

try:
    import microphone
except ImportError:
    print("Warning: `microphone` must be installed in order to use `audio_identification`")

try:
    import eyed3
except ImportError:
    print("Warning: `eyed3` must be installed in order to use `audio_identification`")

try:
    import librosa
except ImportError:
    print("Warning: `librosa` must be installed in order to use `audio_identification`")

setup(name='audio_identification',
      version='1.0',
      description='Identifies audio samples',
      authors='Petar Griggs (@Anonymission), Michael Lai (@impostercafe), Amanda Wang (@CandyMandy28), Anthony Cavallaro (@QuantatativeFinancier)',
      author_email="marrs2k@gmail.com",
      packages=find_packages(),
      license="MIT"
      )
