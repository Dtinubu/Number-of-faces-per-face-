import numpy as np
import argparse
import cv2
import os
import cvlib as cv

images_root = os.path.join('/cmlscratch','dtinubu','datasets','RFW','Balancedface','race_per_7000', args.race)
names = os.listdir(images_root)
for klass, name in enumerate(names):
		  image_path = os.path.join(images_root, name)
		  images_of_person = os.listdir(os.path.join(images_root, name))
		  for  i in range (len(images_of_person)):
                    path =  os.path.join(images_root, name, images_of_person[i])
		    # read input image
                    image = cv2.imread(path)
                    if image is None:
                      print("Could not read input image")
                      exit()
                      faces, confidences = cv.detect_face(image) 
                      label, confidence = cv.detect_gender(face)
                      f = open(args.text_file+".txt","a")
                      f.write(label + "," + name + "," + path + "\n")
                      print(label + "," + name + "," + path + "\n")
                      f.close()
