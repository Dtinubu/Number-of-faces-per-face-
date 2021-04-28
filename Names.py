import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os
import cvlib as cv
import statistics

ap = argparse.ArgumentParser()
args = ap.parse_args()
number_of_pic = 0
count=0

Races =  ('Caucasian','Indian','Asian','African')
for race in Races:
            images_root = os.path.join('/cmlscratch','dtinubu','datasets','RFW','Balancedface','race_per_7000', race)
            temp=[]
            names = os.listdir(images_root)
            for klass, name in enumerate(names):
                image_path = os.path.join(images_root, name)
                images_of_person = os.listdir(os.path.join(images_root, name))
                pic_dir = len(os.listdir(image_path))
                number_of_pic+= pic_dir
                temp.append(pic_dir)
            count= count + 1
            data=temp
            data=np.sort(data)
            plt.plot(data,label = race)
            plt.legend()

plt.savefig('data.png')
