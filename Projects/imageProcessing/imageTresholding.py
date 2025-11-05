import cv2
img=cv2.imread(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\flower.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threst=cv2.threshold(gray,80,255,cv2.THRESH_BINARY)
cv2.imshow('IMG',img)
cv2.imshow('GRAY',gray)
cv2.imshow('THRESH_BINARY',threst)
cv2.waitKey(0)
cv2.destroyAllWindows()