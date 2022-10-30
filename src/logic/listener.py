from typing import Tuple
import pyaudio
import time
import numpy as np
import matplotlib.pyplot as plt
import translater

t = translater.Translater()

f,ax = plt.subplots(2)

x = np.arange(10000)
y = np.random.randn(10000)

li, = ax[0].plot(x, y)
ax[0].set_xlim(0,1000)
ax[0].set_ylim(-5000,5000)
ax[0].set_title("Raw Audio Signal")

li2, = ax[1].plot(x, y)
ax[1].set_xlim(0,5000)
ax[1].set_ylim(-100,100)
ax[1].set_title("Fast Fourier Transform")

plt.pause(0.01)
plt.tight_layout()


def create_stream(data_format: int, sample_rate: int) -> Tuple[pyaudio.PyAudio, pyaudio.Stream]:

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format = data_format,
        rate = sample_rate,
        channels = 1,
        input = True
    )

    return audio, stream


def listen(stream: pyaudio.Stream, sample_rate: int, chunk_size: int):
    
    wait = 1.0 / sample_rate

    window = float(sample_rate) / chunk_size
    fft_size = (chunk_size / 2) + 1 if chunk_size % 2 == 0 else (chunk_size + 1) / 2
    
    raw_x = np.arange(chunk_size)
    fft_x = np.arange(fft_size) * window

    stream.start_stream()

    while True:

        try:
            data = stream.read(chunk_size)
            (raw, fft) = t.translate(data, chunk_size)

            li.set_xdata(raw_x)
            li.set_ydata(raw)

            li2.set_xdata(fft_x)
            li2.set_ydata(fft)

            plt.pause(wait)
    
        except Exception as e:
            print(e)
            break 

    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    (audio, stream) = create_stream(pyaudio.paInt16, 44100)

    try:
        listen(stream, 44100, 2048)

    except Exception as e:
        print(e)

        stream.stop_stream()
        stream.close()
        audio.terminate()