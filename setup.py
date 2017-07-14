from distutils.core import setup
from setuptools import find_packages

try:
    import pyaudio
except ImportError:
    print("Warning: `pyaudio` must be installed in order to use `microphone`")

setup(name='audio_identification',
      version='1.0',
      description='Identifies audio samples',
      author='Petar Griggs (@Anonymission)',
      author_email="marrs2k@gmail.com",
      packages=find_packages(),
      license="MIT"
      )
