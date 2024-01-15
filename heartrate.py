import numpy as np
import matplotlib.pyplot as plt

# Generate sample HRV data
sr = 1000  # Sampling rate in Hz
duration = 30  # Duration in seconds
time = np.linspace(0, duration, int(sr * duration), endpoint=False)  # Time vector

# Generating synthetic HRV signal
hrvdata = np.sin(2 * np.pi * 0.2 * time) + 0.5 * np.sin(2 * np.pi * 0.5 * time)

# Applying fast fourier transform
fft_result = np.fft.fft(hrvdata)
freq = np.fft.fftfreq(len(hrvdata), 1/sr)

# Computing PSD
psd = np.abs(fft_result) ** 2

# Normalize PSD
psd_normalized = psd / np.sum(psd)

# Ploting the results
plt.figure(figsize=(10, 6))

# Ploting HRV data separately
plt.subplot(2, 1, 1)
plt.plot(time, hrvdata)
plt.title('HRV Signal')
plt.xlabel('Time (s)')

# Ploting normalized PSD seperately 
plt.subplot(2, 1, 2)
plt.plot(freq, psd_normalized)
plt.title('Normalized Power Spectral Density')
plt.xlabel('Frequency (Hz)')
plt.xlim(0, 2)  # Adjust the frequency range as needed
plt.tight_layout()
plt.show()
