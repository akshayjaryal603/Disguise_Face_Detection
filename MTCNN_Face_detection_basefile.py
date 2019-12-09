from scipy import misc
import sys
import os
import argparse
import tensorflow as tf
import numpy as np
import all_functions
import detect_face
import cv2
def main(args):
	input_path = '/home/mmlab/Face_Reco_Tool_CDOT/Surya_Data/MTCNN_test/11715.jpg'
	#output_path = '/home/mmlab/Surya_Data/Facenet/Face_Recognition_Tool/MTCNN_Face_detection_Tensorflow/' 
	with tf.Graph().as_default():
        	gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpu_memory_fraction)
        	sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))		
		with sess.as_default():
	            pnet, rnet, onet = detect_face.create_mtcnn(sess, None)
	minsize = 20 # minimum size of face
    	threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    	factor = 0.709 # scale factor
	img = misc.imread(input_path)
	if img.ndim == 2:
        	img = all_functions.to_rgb(img)                        
	img = img[:,:,0:3]
	img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
	print(bounding_boxes)
	for x in range(bounding_boxes.shape[0]):
		det = bounding_boxes[x,0:4]
		print(det)
		x1 = int(det[0])
		y1 = int(det[1])
		x2 = int(det[2])
		y2 = int(det[3])
		cv2.rectangle(img_copy,(x1,y1),(x2,y2),(0,0,255),2)
		new_img = img_copy[int(det[1]):int(det[3]),int(det[0]):int(det[2])]
	#img_copy = cv2.resize(img_copy,(1300,800))
	cv2.imshow('image',img_copy) #imshow is for displaying image on screen write subsequent 3 lines
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
	cv2.imwrite('r.png',img_copy) #for saving write one line
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('--input_path',type=str)
	parser.add_argument('--output_path',type=str)
    	parser.add_argument('--image_size', type=int,
        	help='Image size (height, width) in pixels.', default=182)
    	parser.add_argument('--margin', type=int,
        	help='Margin for the crop around the bounding box (height, width) in pixels.', default=44)
    	parser.add_argument('--random_order', 
        	help='Shuffles the order of images to enable alignment using multiple processes.', action='store_true')
    	parser.add_argument('--gpu_memory_fraction', type=float,
        	help='Upper bound on the amount of GPU memory that will be used by the process.', default=1.0)
    	return parser.parse_args(argv)
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
