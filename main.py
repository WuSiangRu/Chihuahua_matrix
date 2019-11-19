import cv2
import numpy as np

if __name__ == '__main__':
    img1=cv2.imread("pic/g1.jpg")
    combine_img=None
    for x in np.arange(4):
        image=None
        for y in np.arange(4):
            if y==0:
                image = img1
            else:
                image=np.concatenate((image,img1))
        if x==0:
           combine_img=image
        else:
            combine_img=np.concatenate((combine_img,image),axis=1)
    cv2.imwrite("pic/combine.jpg",combine_img)
    cv2.waitKey(0)