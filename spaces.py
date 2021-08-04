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

plt.imshow(img)
plt.show()

#bgr to rgb

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
plt.imshow(rgb)
plt.show()

#hsv to gray

hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
hsv_gray=cv.cvtColor(hsv_bgr,cv.COLOR_BGR2GRAY)
cv.imshow("hsv to gray",hsv_gray)

cv.waitKey(0)
cv.destroyAllWindows()
