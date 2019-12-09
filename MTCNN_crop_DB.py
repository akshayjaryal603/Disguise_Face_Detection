from scipy import misc
import sys
import os
import argparse
import tensorflow as tf
import numpy as np
import all_functions
import detect_face
import cv2
import ntpath
def main(args):
	 
	with tf.Graph().as_default():
		gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpu_memory_fraction)
		sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))		
		with sess.as_default():
			pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

	minsize = 60 # minimum size of face
	threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
	factor = 0.9 # scale factor
	input_path=args.input_path
	img = misc.imread(input_path)

	if img.ndim == 2:
        	img = all_functions.to_rgb(img)                        
	img = img[:,:,0:3]
	img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
	bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
	
	for x in range(bounding_boxes.shape[0]):
		det = bounding_boxes[x,0:4]
		det_ind = det < 0
		det[det_ind] = 0
		
		input_p = input_path[:(len(input_path)-4)]+'_'+str(x)+input_path[(len(input_path)-4):]
		inputp1 = ntpath.basename(input_p)
		inputp2 = ntpath.dirname(input_path)
		temp_path = inputp2+'/Face_crops/' #create a folder named Face_crops in the database folder
		outpath = temp_path + inputp1

		x1 = int(det[0])
		y1 = int(det[1])
		x2 = int(det[2])
		y2 = int(det[3])

		new_img_face = img_copy[y1:y2,x1:x2]		
		cv2.imwrite(outpath,new_img_face)
		#cv2.rectangle(img_copy,(x1,y1),(x2,y2),(0,0,255),5) #comment if we do not need rectangle on the original image		
		

	cv2.imwrite(args.output_path,img_copy)

def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('--input_path',type=str)
	parser.add_argument('--output_path',type=str)
	parser.add_argument('--image_size', type=int,
        	help='Image size (height, width) in pixels.', default=182)
	parser.add_argument('--margin', type=int,
        	help='Margin for the crop around the bounding box (height, width) in pixels.', default=100)
	parser.add_argument('--random_order', 
        	help='Shuffles the order of images to enable alignment using multiple processes.', action='store_true')
	parser.add_argument('--gpu_memory_fraction', type=float,
        	help='Upper bound on the amount of GPU memory that will be used by the process.', default=1.0)
	return parser.parse_args(argv)
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
