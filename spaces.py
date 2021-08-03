import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('photos/people.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#from bgr to l*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#plt.imshow(img)
#plt.show()

#bgr to rgb

rbg=cv.cvtColor(img,cv.CLOR)

cv.waitKey(0)
cv.destroyAllWindows()
