import pyaudio
import numpy as np
import math
import time
from scipy.signal import find_peaks

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

p = pyaudio.PyAudio()

def record_audio():
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    
    frames = []
    
    # Record audio for 5 seconds
    for i in range(0, int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    
    audio = np.frombuffer(b''.join(frames), dtype=np.int16)
    return audio

def get_peak_frequency(audio):
    # Apply Fourier transform
    fourier = np.fft.fft(audio)
    
    # Take the absolute value of the complex values output by the FFT
    abs_fourier = np.abs(fourier)
    
    # Find the frequencies corresponding to each element of the FFT output
    freqs = np.fft.fftfreq(len(abs_fourier)) * RATE
    
    # Find the peak frequencies in the FFT output
    peaks, _ = find_peaks(abs_fourier, height=100000)
    
    if len(peaks) > 0:
        peak_freq = freqs[peaks][0]
        return peak_freq
    else:
        return None

# Listen for audio input and play the corresponding buzzer tone
while True:
    audio = record_audio()
    peak_freq = get_peak_frequency(audio)
    
    if peak_freq is not None:
        # Map the frequency to a corresponding tone for the buzzer
        tone = int(20 * math.exp(0.057 * peak_freq))
        print("Playing tone:", tone)
        
        # Send the tone to the buzzer
        # [INSERT ARDUINO CODE HERE]
        
    time.sleep(0.1)