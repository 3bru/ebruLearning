import numpy as np
import cv2


photo = cv2.imread('kare.jpg')
grayPhoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
grayPhoto = np.float32(grayPhoto)

corner = cv2.goodFeaturesToTrack(grayPhoto, 100,0.01,10)
corner = np.int0(corner)

for kose in corner:
    x,y = kose.ravel()
    cv2.circle(photo,(x,y),3,255,-1)

cv2.imshow('corner',photo)
cv2.waitKey(0)
cv2.destroyAllWindows()