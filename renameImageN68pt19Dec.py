import os
import glob as g

lof=g.glob('*.jpg')
for i in range(len(lof)):
    lof[i]= lof[i].split('.')[0]

for i in range(len(lof)):
     os.rename(str(lof[i]+".jpg"), "occluded"+str(i)+".jpg")
     os.rename(str(lof[i]+".68pt"),"occluded"+str(i)+".68pt")
