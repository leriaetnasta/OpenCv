import cv2 as cv

img=cv.imread('photos/puppy.jpg')

#cv.imshow('puppy',img)

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

image_resized=rescale(img,0.2)
cv.imshow('resized image',image_resized)

capture=cv.VideoCapture('videos/video.mp4')

while True:
    isTrue, frame =capture.read()
    frame_resized=rescale(frame)
    #cv.imshow('video',frame)
    #cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) &  0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()