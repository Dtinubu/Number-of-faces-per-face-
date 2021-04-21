import matplotlib.pyplot as plt
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
number_of_pic = 0
count=0
temp=[]
images_root = os.path.join('/cmlscratch','dtinubu','datasets','RFW','Balancedface','race_per_7000', args.race)
names = os.listdir(images_root)
for klass, name in enumerate(names):
        image_path = os.path.join(images_root, name)
        images_of_person = os.listdir(os.path.join(images_root, name))
        pic_dir = len(os.listdir(image_path))
        number_of_pic+= pic_dir
        temp.append(pic_dir)
        count= count + 1
                  
data=temp		
np.sort(data)
plt.plot(data)
plt.show()
plt.savefig(args.race + '_spread.png')
print("mean " + str(statistics.mean(data)))
print("median " + str(statistics.median(data)))
print("mode "+ str(statistics.mode(data)))

