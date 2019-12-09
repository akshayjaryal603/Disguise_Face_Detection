from PIL import Image
import scipy.fftpack as fp
import numpy as np
import matplotlib.pyplot as plt
import glob as g

lofn= g.glob('normal*.jpg')
lofo= g.glob('occluded*.jpg')
n=len(lofn)
o=len(lofo)

for i in range(1, n+1):
    a=np.array(Image.open(lofn[i-1]).convert('L'))
    anew= abs(fp.fft(a))
    plt.subplot(1,n+1,i)
    plt.plot(anew)
 
for i in range(1, o+1):
    a=np.array(Image.open(lofo[i-1]).convert('L'))
    anew= abs(fp.fft(a))
    plt.subplot(1,n+1,i)
    plt.plot(anew)   

plt.show()

