import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models'))
import utilFunctions as UF


# convert the duration of the first half and second half of the signal. 
# Allows us to handle even and odd-sized values so we know
# where the middle of the window is.
M = 501
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

(fs, x) = UF.wavread('/home/jeffreymartin/Documents/source/source/sms-tools/sounds/soprano-E4.wav')  # reads the file and converts it to floating point numbers -1 to 1
x1 = x[5000:5000+M] * np.hamming(M)  # we take a fragment of the signal (501 samples)

# we will center the signal around 0 in the fft buffer, adding zero-padding
N = 1024
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
# make the magnitude spectrum in dB
mX = 20*np.log10(abs(X))
pX = np.unwrap(np.angle(X))

# plot half of the magnitude spectrum
# plt.plot(mX[0:512])
# plt.show()

# plot the phase, unwrapping the angles
plt.plot(pX)
plt.show()