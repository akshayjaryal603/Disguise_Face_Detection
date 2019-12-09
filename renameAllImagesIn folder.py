import glob as g
import os

i=1
lof=g.glob('*.jpg')
for fname in lof:
	os.rename(fname,'normalFacesF'+str(i)+'.jpg')
	i=i+1

lof=g.glob('*.png')
for fname in lof:
	os.rename(fname,'normalFacesF'+str(i)+'.png')
	i=i+1

lof=g.glob('*.jpeg')
for fname in lof:
	os.rename(fname,'normalFacesF'+str(i)+'.jpeg')
	i=i+1
