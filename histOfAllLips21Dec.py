from skimage import feature
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob as g
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fnames=g.glob('*.jpg')
arr=['r' if i.startswith('occlude') else 'b' for i in fnames]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for c, z, imgn in zip(arr, [i*10 for i in range(len(fnames))], fnames):
    image = cv2.imread(imgn);	
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
    lbp = feature.local_binary_pattern(image,16,2, method="uniform")
    (hist, _) = np.histogram(lbp.ravel())
    hist = hist.astype("float")
    hist /= hist.sum()
    xs = np.arange(len(hist))
    ys = hist
    cs = [c] * len(xs)
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
