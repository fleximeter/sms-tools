import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)  # a triangular waveform
fftbuffer = np.zeros(15)  # a zero buffer
fftbuffer[:8] = x[7:]     # put the first part of the triangle at the end of the buffer
fftbuffer[8:] = x[:7]     # put the last part of the triangle at the beginning of the buffer
X = fft(fftbuffer)  # if you don't supply a signal with a length a power of 2, it uses the DFT instead
mX = abs(X)  # magnitude
pX = np.angle(X)  # phase

# plot the waveform
# plt.plot(fftbuffer)
# plt.show()

# plot the magnitude spectrum. This plots it in positive-negative form. It has not changed from the previous version.
# plt.plot(mX)
# plt.show()

# plot the phase spectrum. This is different from the previous version.
plt.plot(pX)
plt.show()
