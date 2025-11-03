import cv2
import numpy as np
img=cv2.imread(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\flower.jpg')
# transform=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('IMG',img)
# cv2.imshow('transform',transform)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def myCvtColor(img):
    img_new=np.mean(img,axis=2)
    img_new=np.array(img_new,dtype=np.uint8)
    print(img.shape,img_new.shape)
    return img_new
transformed=myCvtColor(img)
cv2.imshow('transform',transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

