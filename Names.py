import numpy as np
import argparse
import cv2
import os
import cvlib as cv
import statistics

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--race", required=True,
	help="path to input image")
args = ap.parse_args()
 Number_of_pic = 0
count=0
temp=[]
images_root = os.path.join('/cmlscratch','dtinubu','datasets','RFW','Balancedface','race_per_7000', args.race)
names = os.listdir(images_root)
	for klass, name in enumerate(names):
		  image_path = os.path.join(images_root, name)
		  images_of_person = os.listdir(os.path.join(images_root, name))
		  Pic_dir=len(os.listdir( image_path))
		  Number_of_pic+= Pic_dir
		  temp.append(Pic_dir)
		  Count++
                  
		
	data=temp
	plt.boxplot(data)
	print(count)
	print(Number_of_pic/count)
	print("median" + statistics.median(data))
	print("mode"statistics.mode(data))
	plt.show()
