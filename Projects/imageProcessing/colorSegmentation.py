import cv2
import numpy as np
frame=cv2.imread(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\colors3.jpg')
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_color=np.array([96,227,130])
upper_color=np.array([140,255,255])

mask=cv2.inRange(hsv,lower_color,upper_color)
res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow('res',res)
cv2.imshow('mask',mask)
cv2.imshow('frame',frame)
cv2.imshow('hsv',hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

