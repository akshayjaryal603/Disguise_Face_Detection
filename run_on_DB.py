import os

with open('filepaths.txt') as f:
	for line in f:
		a = line.rstrip()
		os.system("python MTCNN_crop_DB.py --input_path "+a+" --output_path "+a)
