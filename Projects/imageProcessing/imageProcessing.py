import cv2
# img=cv2.imread(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\flower.jpg')
# # print(img.shape,img.ndim,type(img))
# img[:,100]=[255,255,255]
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
source=cv2.VideoCapture(r'C:\Users\buthm\Downloads\drive-download-20251102T091203Z-1-001\codes\Samples\road_drive.avi')
while(True):
    ret,img=source.read()
    print(ret)
    if(ret==False):
        break
    cv2.imshow('IMG',img)
    cv2.waitKey(1)
cv2.destroyAllWindows()