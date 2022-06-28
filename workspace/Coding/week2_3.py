import numpy as np
import matplotlib.pyplot as plt

# This example implements the DFT, using a complex signal.

N = 64

# A signal to run through the DFT
k0 = 7
x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))

X = np.array([])  # holds the output spectral samples

for k in range(N):  # k from 0 to N-1
    s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
    X = np.append(X, np.sum(x * np.conjugate(s)))

# Plot the result
plt.plot(np.arange(N), abs(X))
plt.axis([0, N - 1, 0, N])
plt.show()

# the result is 64 at index 7.
