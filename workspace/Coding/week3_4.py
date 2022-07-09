import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import dftModel as DFT

(fs, x) = UF.wavread('/home/jeffreymartin/Documents/source/source/sms-tools/sounds/piano.wav')  # reads the file and converts it to floating point numbers -1 to 1

M = 511
w = get_window('hamming', M)
time = 0.2  # start at 0.2 seconds
x1 = x[int(time * fs) : int(time * fs) + M] # convert to samples - the samples of x that start at 0.2 seconds and lasts for M samples
N = 1024
mX, pX = DFT.dftAnal(x1, w, N)  # mX is the positive side of the spectrum, pX is the unwrapped phase spectrum
y = DFT.dftSynth(mX, pX, w.size) * sum(w)

plt.plot(mX)
plt.show()
