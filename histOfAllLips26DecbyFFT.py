import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fp
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glob as g

im2freq = lambda data: fp.rfft(fp.rfft(data, axis=0), axis=1)
remmax = lambda x: x/x.max()
remmin = lambda x: x - np.amin(x, axis=(0,1), keepdims=True)
touint8 = lambda x: (remmax(remmin(x))*(256-1e-4)).astype(int)

fnames=g.glob('*.jpg')
arr=['r' if i.startswith('occlude') else 'b' for i in fnames]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for c, z, imgn in zip(arr, [i*10 for i in range(len(fnames))], fnames):
    image = np.array(Image.open(imgn).convert('L'))
    ci= im2freq(image); # print len(ci.ravel())
    ci= touint8(ci)
    ci=ci.ravel()
    (hist, _) = np.histogram(ci, bins=range(0, 256))
    #print(hist)
    hist = hist.astype("float")
    hist /= hist.sum()
    xs = np.arange(len(ci))
    ys =ci
    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
    
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
