import cv2 as cv


img=cv.imread('photos/people.jpeg')
cv.imshow('img',img)

#split into blue green and red with split fct
b,g,r=cv.split(img)

cv.imshow('bleu',b)
cv.imshow('red',r)
cv.imshow('green',g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

cv.waitKey(0)
cv.destroyAllWindows()