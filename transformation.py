import cv2 as cv
import numpy as np
img=cv.imread('photos/puppy.jpg')
#cv.imshow('puppy',img)

def transformation(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
#pos y :down neg y :up
#pos x :right neg x :left

trans=transformation(img,-200,-200)
#cv.imshow('translated',trans)
#rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(height,width)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)

#cv.imshow('rotated',rotated)

rotated_rotated=rotate(rotated,-15)
#cv.imshow('rotated rotated',rotated_rotated)

#resize
resized=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('resized',resized)

#flipped
flipped=cv.flip(img,1)
#cv.imshow('flipped',flipped)

#cropped img[y:y+h, x:x+w]
cropped=img[img.shape[0]//2:img.shape[0],img.shape[1]//2:img.shape[1]]
cv.imshow('cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()