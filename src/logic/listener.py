from typing import Tuple
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import translater

def create_stream(data_format: int, sample_rate: int) -> Tuple[pyaudio.PyAudio, pyaudio.Stream]:

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format = data_format,
        rate = sample_rate,
        channels = 1,
        input = True
    )

    return audio, stream


def listen(stream: pyaudio.Stream, t: translater.Translater, ax, raw_ax, fft_ax):
    
    sample_rate = t.sample_rate
    chunk_size = t.chunk_size

    wait = 1.0 / sample_rate
    
    raw_x = np.arange(chunk_size)
    fft_x = np.arange(t.n_bins) * t.bin_size

    # Set up plots
    ax[0].set_xlim(0, 1000)
    ax[0].set_ylim(-5000, 5000)
    ax[0].set_title("Raw Audio Signal")

    ax[1].set_xlim(0, t.n_bins * t.bin_size)
    ax[1].set_ylim(0, 100)
    ax[1].set_title("Fast Fourier Transform")

    plt.pause(0.01)
    plt.tight_layout()

    # Start listening
    stream.start_stream()

    while True:

        try:
            data = stream.read(chunk_size)
            (raw, fft) = t.translate(data)

            raw_ax.set_xdata(raw_x)
            raw_ax.set_ydata(raw)

            fft_ax.set_xdata(fft_x)
            fft_ax.set_ydata(fft)

            plt.pause(wait)
    
        except Exception as e:
            print(e)
            break 

    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    # Set up plots with random data
    f, ax = plt.subplots(2)

    x = np.arange(10000)
    y = np.random.randn(10000)

    raw_ax, = ax[0].plot(x, y)
    fft_ax, = ax[1].plot(x, y)

    # Set up stream and translater
    (audio, stream) = create_stream(pyaudio.paInt16, 44100)
    t = translater.Translater(44100, 2048)

    # Start listening
    try:
        listen(stream, t, ax, raw_ax, fft_ax)

    except Exception as e:
        print(e)

        stream.stop_stream()
        stream.close()
        audio.terminate()