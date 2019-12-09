import cv2
import os
with open('filepaths.txt') as f:
    for line in f:
	I = cv2.imread(line.rstrip())
	if I.shape[0] >= 60 or I.shape[1] >= 60:
		I1 = cv2.resize(I,(160, 160))
		cv2.imwrite(line.rstrip(),I1)
	else:
		os.system("rm "+line.rstrip()) # smaller than 160,160 remove
		#os.system("mv "+line.rstrip()+' /home/mmlab/Snigdha_Data/MTCNN/test_database/small_crops/') # smaller crops are copied to small_crops folder

	
