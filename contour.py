import cv2 as cv
import numpy as np 


img = cv.imread('photos/people.jpeg')

cv.imshow('people',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grap',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#list of all the contours 
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

blank=np.zeros(img.shape,dtype='uint8')
#draw the contours on the blank image (-1 means all of the contours)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours',blank)

cv.waitKey(0)
cv.destroyAllWindows()
