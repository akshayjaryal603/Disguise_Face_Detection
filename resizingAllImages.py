from PIL import Image
import glob as g
import os, sys
lof=[]
s=['*.jpg','*.png','*.jpeg']
for i in s:
    lof.extend(g.glob(i))

n=len(lof)

def resize():
    for i in range(0, n-1):
        im= Image.open(lof[i])
        im=im.resize((256, 256))
        im.save(lof[i])

resize()
