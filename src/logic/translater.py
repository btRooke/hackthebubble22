from typing import List, Tuple
import numpy as np
from scipy.stats import mode

class Translater:

    def __init__(self, sample_rate: int, chunk_size: int):
        # Stream parameters
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size

        # FFT parameters
        self.bin_size = float(sample_rate) / chunk_size
        self.n_bins = (chunk_size / 2) + 1 if chunk_size % 2 == 0 else (chunk_size + 1) / 2
        self.fft_time = (1.0 / sample_rate) * chunk_size
        
        # Translation parameters
        self.history = []


    # Take a chunk of samples and attempt to translate them
    def translate(self, data: List[np.int16]) -> Tuple[List[np.int16], List[np.int16]]:

        # Convert data to numpy format
        np_data = np.fromstring(data, np.int16)
        
        # Fast Fourier Transform
        transformed = np.fft.rfft(np_data)

        # Match data to the decibel scale, discarding imaginary values
        scaled = 10.0 * np.log10(abs(transformed))

        self.try_add(scaled)
        return np_data, scaled


    # Decide whether to add the FFT result to history
    def try_add(self, fft: List[np.int16]) -> bool:
        # Find the loudest frequency and the 90th-percentile amplitude
        percentile = np.percentile(fft, 90)
        peak = np.argmax(fft)

        #print("90th percentile: " + str(percentile) + ", peak: " + str(fft[peak]))

        # If the loudest frequency is not significantly above the 90th percentile, ignore it
        if fft[peak] - percentile < 20:
            return self.evaluate_history()
        
        # If the loudest frequency does not match the history, a new character has been started
        elif len(self.history) > 0 and abs(peak - self.history[-1][0]) > 2:
            return self.evaluate_history()
            

        # Otherwise, add the FFT result to the history
        else:
            self.history.append((peak, fft[peak]))
        

    # Check whether the history array represents a consistent frequency for a significant time period
    def evaluate_history(self):
        # Discard short length (< 0.2s)
        if len(self.history) * self.fft_time < 0.2:
            self.history.clear()
            return False

        # Find most common frequency
        m = mode([x[0] for x in self.history])[0] * self.bin_size
        print(m)

        self.history.clear()
        return True

        