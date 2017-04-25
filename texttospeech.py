import pyttsx
from .engine import Engine
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()