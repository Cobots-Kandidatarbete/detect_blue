import cv2
import pyrealsense2 as rs
import numpy as np
from realsense_depth import *

"""
import SimpleCV
from SimpleCV import Camera
import time

cam = Camera()
time.sleep(3)

img = cam.getImage()

"""

#cam = cv2.VideoCapture(1) #cv2.CAP_DSHOW)


'''
contador = 0 
while True:
    check, img = cam.read()
    #cv2.imshow("Captura", frame)
    key = cv2.waitKey(1)
    if contador==10:                     #Low contador means low light
        cv2.imwrite(filename='image.png', img=img)
        break
    contador=contador+1
    
cam.release()
'''

  
# reading the input using the camera
#result, img = cam.read()
#if not result:
   #raise ValueError("Cam not found")



#img_org = cv2.imread("lada.jpg")
#img = cv2.resize(img_org, (600,800))
lower_range = np.array([100, 128, 0])
upper_range = np.array([215, 255, 255])


while True:

   depth_cam = DepthCamera()

   ret, depth_frame, img = depth_cam.get_frame()

   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

   mask = cv2.inRange(hsv, lower_range, upper_range)

   x, y = np.where(mask == 255)

   mean_yx = [round(np.mean(y)), round(np.mean(x))]


   #img[mean_x:mean_x+5, mean_y:mean_y+5] = [0,255,0]

   cv2.circle(img,mean_yx, 4, (0, 0, 255))

   distance = depth_frame[mean_yx[1],mean_yx[0]]

   print(distance)

   cv2.imshow('image', img)

   key = cv2.waitKey(1)

   if key == 27:
      break


#cv2.imshow('mask', mask)


'''
while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()
'''