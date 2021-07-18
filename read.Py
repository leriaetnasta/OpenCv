import cv2 as cv

#img=cv.imread('photos/puppy.jpg')

#cv.imshow('puppy',img)

#cv.waitKey(0)

capture=cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame =capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) &  0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()