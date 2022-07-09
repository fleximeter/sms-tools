import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)  # a triangular waveform

X = fft(x)  # if you don't supply a signal with a length a power of 2, it uses the DFT instead
mX = abs(X)  # magnitude
pX = np.angle(X)  # phase

# plot the waveform
# plt.plot(x)
# plt.show()

# plot the magnitude spectrum. This plots it in positive-negative form.
# plt.plot(mX)
# plt.show()

# plot the phase spectrum. It is not centered around 0 because the 
# triangle wave was not centered at 0. In the next file we will fix this.
plt.plot(pX)
plt.show()
