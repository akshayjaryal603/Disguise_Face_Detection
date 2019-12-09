import glob as g
import os
from PIL import Image as ii

i=1
lof=g.glob('*.jpg')
for fname in lof:
	a=ii.open(fname).convert('L')
	os.remove(fname)
	a.save(fname)

lof=g.glob('*.png')
for fname in lof:
	a=ii.open(fname).convert('L')
	os.remove(fname)
	a.save(fname)

lof=g.glob('*.jpeg')
for fname in lof:
	a=ii.open(fname).convert('L')
	os.remove(fname)
	a.save(fname)

