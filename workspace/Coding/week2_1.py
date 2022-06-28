import matplotlib.pyplot as plt
import numpy as np

# This example is a real sinusoid

A = .8           # the amplitude
f0 = 1000        # the frequency
phi = np.pi / 2  # the phase
fs = 44100       # the sampling rate

# creates an array of floats from -0.002 to 0.002 in increments of 1/fs
t = np.arange(-0.002, 0.002, 1.0/fs) 
x = A * np.cos(2 * np.pi * f0 * t + phi)

plt.plot(t, x)
plt.axis([-0.002, 0.002, -0.8, 0.8])
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
