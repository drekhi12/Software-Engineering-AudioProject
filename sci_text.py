from scipy.io import wavfile
from pylab import *
from constants import *
 
class AudioAnalysis(object):
  
    LEVEL_THRESHOLD = 0.3 
    SLICE_SIZE = 2205
    MAYBE_PATTERN = [3,2,1]
 
    def speech_to_text(self, wave_file):
          
        # read voice file
        rate, data = wavfile.read(wave_file)
        data = data / (2.**15)
  
        # get blob indices and count
        blob_indices = self._blob_indices(data)
        blob_count = len(blob_indices)
 
        # get pattern match
        is_pattern_match = False
        if blob_count == 2:
            is_pattern_match = self._is_pattern_match(data[blob_indices[1]:], self.MAYBE_PATTERN)
 
        # return speech to text
        if blob_count == 1:
            return NO
        elif blob_count == 2 and is_pattern_match:
            return MAYBE
        elif blob_count == 2 and not is_pattern_match:
            return YES
        else:
            return ""