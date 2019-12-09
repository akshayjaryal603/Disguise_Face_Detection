from skimage import feature
import cv2
import numpy as np
import matplotlib.pyplot as plt


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for c, z, imgn in zip(['b', 'r'], [10, 0], ['a.jpg', 'b.jpg']):
    image = cv2.imread(imgn);	
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
    lbp = feature.local_binary_pattern(image, 24,3, method="uniform")
    (hist, _) = np.histogram(lbp.ravel())
    hist = hist.astype("float")
    hist /= hist.sum()
    xs = np.arange(len(hist))
    ys = hist
    print(xs,"-----------", ys)
    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
