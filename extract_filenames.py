import os

a = open("filepaths.txt", "w")
for path, subdirs, files in os.walk('H:\ECT-FaceAlignment-master\MTCNN\database01'):
   for filename in files:
     f = os.path.join(path, filename)
     a.write(str(f) + os.linesep) 
