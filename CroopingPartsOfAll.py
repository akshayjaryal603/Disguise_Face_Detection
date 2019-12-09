import os
import glob as g
import shutil as sh # shell utilities

now= os.getcwd()

os.chdir(now+'/downloads/imgsMarked/')
lod= g.glob('*')
n=len(lod)
os.chdir(now)

for i in range(n):
    a= now+'/downloads/imgsMarked/'+ str(lod[i])
    sh.copytree(a, now+'/img/')
    sh.copy('cropPartsfromFace20Dec.py', now+'/img/')
    os.chdir(now+'/img/')
    os.system('python cropPartsfromFace20Dec.py')
    os.remove('cropPartsfromFace20Dec.py')
    os.chdir(now)
    sh.copytree(now+'/img/', now+'/img_ResultsCropped_For'+ str(lod[i])+'/')
    sh.rmtree(now+'/img/')


