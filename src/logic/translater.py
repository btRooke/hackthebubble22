from typing import List
import numpy as np

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
    def translate(self, data: List[np.int16]):

        # Convert data to float type
        float_data = np.fromstring(data, np.int16)
        
        # Fast Fourier Transform
        transformed = np.fft.rfft(float_data)

        # Match data to the decibel scale, discarding imaginary values
        scaled = 10.0 * np.log10(abs(transformed))

        # Find the loudest frequency and compare it to history
        peak = np.argmax(scaled)

        return float_data, scaled
