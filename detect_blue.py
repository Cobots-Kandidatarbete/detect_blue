import cv2
import numpy as np
import imutils


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  
# reading the input using the camera
result, img = cam.read()
if not result:
   raise ValueError("Cam not found")

"""
img_org = cv2.imread("lada.jpg")
img = cv2.resize(img_org, (600,800))
"""

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()