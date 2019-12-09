from skimage import feature
import cv2
import numpy as np
import matplotlib.pyplot as plt

imgn='b.jpg'
image = cv2.imread(imgn)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lbp = feature.local_binary_pattern(image, 24,3, method="uniform")
(hist, _) = np.histogram(lbp.ravel())
 
# normalize the histogram
hist = hist.astype("float")
hist /= hist.sum()
plt.hist(hist)
plt.show()
