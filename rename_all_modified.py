import cv2
import ntpath
import os
import re
with open('filepaths.txt') as f:
    b=1
    for line in f:
	a = line.rstrip()
	y = (os.path.dirname(a))
	z = os.path.basename(y)
	w = a.find('.')
	print w
	os.rename(a, y+'/'+z+'_'+str(b)+a[w:])
	#print (y+'/'+z+'_'+str(b))
        b=b+1


