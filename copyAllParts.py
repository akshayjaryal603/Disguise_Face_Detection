import os
import glob as g
import shutil as sh
from distutils.dir_util import copy_tree

lod= g.glob('*')
now= os.getcwd()
'''
for i in range(len(lod)):
    try:
        os.chdir(now+'/'+ lod[i] +'/Eyes/')
        lof= g.glob('*.jpg')
        for j in range(len(lof)):
            os.rename(lof[j], lof[j].split('.')[0]+'_'+lod[i]+'.jpg')
        os.chdir(now+'/'+ lod[i] +'/Nose/')
        lof= g.glob('*.jpg')
        for j in range(len(lof)):
            os.rename(lof[j], lof[j].split('.')[0]+'_'+lod[i]+'.jpg')
        os.chdir(now+'/'+ lod[i] +'/Lips/')
        lof= g.glob('*.jpg')
        for j in range(len(lof)):
            os.rename(lof[j], lof[j].split('.')[0]+'_'+lod[i]+'.jpg')
        os.chdir(now)
    except:
        print("haww")
'''              

os.mkdir('AllEyes')
os.mkdir('AllNose')
os.mkdir('AllLips')

for i in range(len(lod)):
    try:
        copy_tree(lod[i] +'/Eyes','AllEyes')
        copy_tree(lod[i] +'/Lips','AllLips')
        copy_tree(lod[i] +'/Nose','AllNose')
    except:
        print("haww")
        
       
