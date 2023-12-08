# This section of the code is licensed under GPL due to phonemizer and espeak-ng

# load phonemizer
import phonemizer

# note: comment this out if not on Windows
from phonemizer.backend.espeak.wrapper import EspeakWrapper
EspeakWrapper.set_library('C:\Program Files\eSpeak NG\libespeak-ng.dll')

global_phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True,  with_stress=True)

def phonemize(text):
    return global_phonemizer.phonemize(text)