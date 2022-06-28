import numpy as np
import matplotlib.pyplot as plt

# This example implements the IDFT, using a real signal.

N = 64
k0 = 7
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])  # holds the output spectral samples
nv = np.arange(-N/2, N/2)  # a normalizer to make the output be properly positioned
kv = np.arange(-N/2, N/2)  # a normalizer to make the output be properly positioned

# The DFT
for k in kv:  # k from 0 to N-1
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, np.sum(x * np.conjugate(s)))

# The IDFT
y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    y = np.append(y, 1.0/N * sum(X * s))

# Plot the result
plt.plot(kv, y)
plt.axis([-N/2, N/2 - 1, -1, 1])
plt.show()

# the result is 2 peaks instead of 1.
