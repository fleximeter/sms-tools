import numpy as np
import matplotlib.pyplot as plt

# This example implements the DFT, using a real signal.

N = 64

# A signal to run through the DFT
k0 = 7  # the input frequency (harmonic). If you don't input an integer, you get positive values
# for all of the spectrum.
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])  # holds the output spectral samples
nv = np.arange(-N/2, N/2)  # a normalizer to make the output be properly positioned
kv = np.arange(-N/2, N/2)  # a normalizer to make the output be properly positioned
print(nv)
print(kv)
for k in kv:  # k from 0 to N-1
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, np.sum(x * np.conjugate(s)))

# Plot the result
plt.plot(kv, abs(X))
plt.axis([-N/2, N/2 - 1, 0, N])
plt.show()

# the result is 2 peaks instead of 1.
