import cv2
import numpy as np
import imutils

"""
import SimpleCV
from SimpleCV import Camera
import time

cam = Camera()
time.sleep(3)

img = cam.getImage()

"""

cam = cv2.VideoCapture(2) #cv2.CAP_DSHOW)



contador = 0 
while True:
    check, img = cam.read()
    #cv2.imshow("Captura", frame)
    key = cv2.waitKey(1)
    if contador==10:                     #Low contador means low light
        cv2.imwrite(filename='image.png', img=img)
        break
    contador=contador+1
    #print(contador)
cam.release()


  
# reading the input using the camera
#result, img = cam.read()
#if not result:
   #raise ValueError("Cam not found")



#img_org = cv2.imread("lada.jpg")
#img = cv2.resize(img_org, (600,800))


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([100,128,0])
upper_range = np.array([215,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()