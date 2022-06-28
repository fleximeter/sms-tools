import matplotlib.pyplot as plt
import numpy as np

# This example is a complex sinusoid

N = 500          # array length, size of DFT
k = 3            # the frequency / number of periods
n = np.arange(-N/2, N/2)  # the time indices
s = np.exp(1j * 2 * np.pi * k * n / N)  # the complex sinusoid

plt.plot(n, np.real(s))  # plots the real part
plt.plot(n, np.imag(s))  # plots the imaginary part
plt.axis([-N/2, N/2, -1, 1])
plt.xlabel("n")
plt.ylabel("amplitude")
plt.show()
