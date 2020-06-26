# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:36:58 2020

@author: HP
"""
#pip install numpy
#pip install opencv-python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=plt.imread(r"C:\Users\HP\Desktop\Face recognisation\images.jpg")
plt.imshow(img)

detector=cv2.CascadeClassifier(r"C:\Users\HP\Desktop\Face recognisation\haarcascade_frontalface_alt.xml")
faces=detector.detectMultiScale(img)
faces
faces.shape
faces[0]
x,y,w,h=faces[0]
x
y
w
h
img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
plt.imshow(img)

#PLOT RECTANGLE FOR ALL FACES

for face in faces:
    x,y,w,h=face
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    plt.imshow(img)




