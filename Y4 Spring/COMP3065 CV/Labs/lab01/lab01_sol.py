#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

### read in input image and convert to gray image
img = cv2.imread('skull.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

### using OpenCV Sobel filter
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

plt.figure()
plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray')
plt.title('Gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


### calculate gradient magnitude and orientation
gMag = (sobelx**2 + sobely**2)**0.5
orien = cv2.phase(np.array(sobelx, np.float64), np.array(sobely, np.float64), angleInDegrees=True)

## map the orientation using 4 colors for visualization
orienMap = np.zeros((orien.shape[0], orien.shape[1], 3), dtype=np.int32)

# Define RGB colours
red = np.array([255, 0, 0])
cyan = np.array([0, 255, 255])
green = np.array([0, 255, 0])
yellow = np.array([255, 255, 0])

# Set colours corresponding to angles
for i in range(0, orienMap.shape[0]):
    for j in range(0, orienMap.shape[1]):
        if orien[i, j] < 90.0:
            orienMap[i, j, :] = red
        elif orien[i, j] >= 90.0 and orien[i, j] < 180.0:
            orienMap[i, j, :] = cyan
        elif orien[i, j] >= 180.0 and orien[i, j] < 270.0:
            orienMap[i, j, :] = green
        elif orien[i, j] >= 270.0 and orien[i, j] < 360.0:
            orienMap[i, j, :] = yellow

plt.figure()
plt.subplot(1,2,1),plt.imshow(gMag,cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(orienMap)
plt.title('Orientation'), plt.xticks([]), plt.yticks([])


### Implement Sobel filter by ourselves
# make sure the data type of the kenel is float to avoid overflow
kenelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype=np.float64)
kenelY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]], dtype=np.float64)

sobelxx = np.zeros(gray.shape)
sobelyy = np.zeros(gray.shape)
h, w = sobelxx.shape
hh, ww = kenelX.shape

## You can do convolution element by element, as shown in lecture notes
#for i in range(hh//2, h-hh//2):
#    for j in range(ww//2, w-ww//2):
#        for ii in range(hh):
#            for jj in range(ww):
#                sobelxx[i,j] += gray[i-hh//2+ii,j-ww//2+jj] * kenelX[ii,jj]
#                sobelyy[i,j] += gray[i-hh//2+ii,j-ww//2+jj] * kenelY[ii,jj]

## or do it using matrix form
for ii in range(hh):
    for jj in range(ww):
        sobelxx[hh//2:h-hh//2, ww//2:w-ww//2] += gray[ii:h-hh+1+ii, jj:w-ww+1+jj] * kenelX[ii,jj]
        sobelyy[hh//2:h-hh//2, ww//2:w-ww//2] += gray[ii:h-hh+1+ii, jj:w-ww+1+jj] * kenelY[ii,jj]

plt.figure()
plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray')
plt.title('Gray'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelxx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobelyy,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

