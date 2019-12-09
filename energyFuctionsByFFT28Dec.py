from PIL import Image
import scipy.fftpack as fp
import numpy as np
import matplotlib.pyplot as plt

a=np.array(Image.open('a.jpg').convert('L'))
b=np.array(Image.open('b.jpg').convert('L'))

anew= abs(fp.fft(a))
bnew= abs(fp.fft(b))

plt.subplot(1,2,1)
plt.plot(anew)
plt.subplot(1,2,2)
plt.plot(bnew)

plt.show()

