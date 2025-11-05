import cv2
import numpy as np
frame=cv2.imread(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\colors3.jpg')
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
cv2.imshow('frame',frame)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

