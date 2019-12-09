import glob as g
import os
from PIL import Image as ii
import sys
import numpy as np
import scipy.misc

padBy= int(sys.argv[1])
i=1
lof=g.glob('*.jpg')
for fname in lof:
	im=ii.open(fname)
	im.load()
	data = np.asarray( im, dtype="int32" )
	data= np.pad(data,(padBy, padBy), 'constant')
	os.remove(fname)
	scipy.misc.imsave(fname, data)

lof=g.glob('*.png')
for fname in lof:
	im=ii.open(fname)
	im.load()
	data = np.asarray( im, dtype="int32" )
	data= np.pad(data,(padBy, padBy), 'constant')
	os.remove(fname)
	scipy.misc.imsave(fname, data)

lof=g.glob('*.jpeg')
for fname in lof:
	im=ii.open(fname)
	im.load()
	data = np.asarray( im, dtype="int32" )
	data= np.pad(data,(padBy, padBy), 'constant')
	os.remove(fname)
	scipy.misc.imsave(fname, data)

