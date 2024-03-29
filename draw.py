import cv2 as cv
import numpy as np

blue= np.zeros((500,500,3),dtype='uint8')
red= np.zeros((500,500,3),dtype='uint8')
green= np.zeros((500,500,3),dtype='uint8')
blank= np.zeros((500,500,3),dtype='uint8')

#cv.imshow('blank',blank)
blue[:]=255,0,0
green[:]=0,255,0
red[:]=0,0,255
cv.rectangle(blue,(125,125),(375,375),(0,0,255))
cv.imshow('blue with red rectangle',blue)
cv.waitKey(0)
cv.rectangle(blue,(125,125),(375,375),(0,0,255),thickness=cv.FILLED)
cv.imshow('blue with red full rectangle',blue)
cv.waitKey(0)
cv.rectangle(green,(125,125),(375,375),(255,0,0),thickness=-1)
cv.imshow('neon green with blue',green)
cv.waitKey(0)
cv.rectangle(red,(red.shape[1]//4,red.shape[1]//4),(red.shape[0]-125,red.shape[0]-125),(255,0,0),thickness=-1)

cv.circle(red,(red.shape[1]//2,red.shape[0]//2),40,(0,0,255),thickness=-1)
cv.line(red,(125,125),(375,375),(0,0,0))
cv.imshow('red with full bleu rectangle',red)
cv.waitKey(0)

cv.putText(blank,"hello, my name is loubna",(5,125),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('blank with text',blank)
cv.waitKey(0)

cv2.destroyAllWindows()


