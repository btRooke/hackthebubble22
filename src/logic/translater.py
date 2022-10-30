import numpy as np

class Translater:

    def translate(self, data, n_frames: int):
        
        # Convert data to float type
        f_data = np.fromstring(data, np.int16)
        
        # Fast Fourier Transform
        transformed = np.fft.rfft(f_data)

        # Match data to the decibel scale, discarding imaginary values
        scaled = 10.0 * np.log10(abs(transformed))

        return f_data / 2, scaled
