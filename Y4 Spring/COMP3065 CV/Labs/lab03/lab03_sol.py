#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

img = cv2.imread('skull.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

## Dominant orientation of a patch

# We take a random patch in the original image
cursor = np.array([30,40]) # center of the patch should be between patchsize/2 and image size - patchsize/2
patchsize = 15
gxPatch = sobelx[cursor[0]-patchsize//2:cursor[0]+patchsize//2, cursor[1]-patchsize//2:cursor[1]+patchsize//2]
gyPatch = sobely[cursor[0]-patchsize//2:cursor[0]+patchsize//2, cursor[1]-patchsize//2:cursor[1]+patchsize//2]

# Compute dominant direction of the patch
sumIx = gxPatch.mean()
sumIy = gyPatch.mean()
patchHessian = np.array([[sumIx**2, sumIx*sumIy], [sumIx*sumIy, sumIy**2]])
error, direction = np.linalg.eig(patchHessian)
directionU = direction[:, np.argsort(error)][0,1] # last column is the dominant direction
directionV = direction[:, np.argsort(error)][1,1]

# To make visualization simple, we draw the rotated patch window instead of actual extract the patch
# rotate the patch window (4 corner points) to along with the dominant direction
# since the eigen vector has unit vector length
sinTheta = directionV
cosTheta = directionU
# rotation matrix
R = np.array([[cosTheta, -sinTheta], [sinTheta, cosTheta]])
pts = np.array([np.dot(R, [-patchsize//2, -patchsize//2]) + cursor,
                np.dot(R, [-patchsize//2, +patchsize//2]) + cursor,
                np.dot(R, [+patchsize//2, +patchsize//2]) + cursor,
                np.dot(R, [+patchsize//2, -patchsize//2]) + cursor], np.int32)
pts.reshape((-1, 1, 2))
# draw the rotated window and dominant direction
img1 = img.copy()
img1 = cv2.polylines(img1, [pts], True, (0, 0, 255), 2, cv2.LINE_AA)
pt = [int(directionU*15), int(directionV*15)] + cursor
# pt = [int(directionU), int(directionV)] + cursor
img1 = cv2.line(img1, tuple(cursor), tuple(pt), (255,0,0), 2)
# img1 = cv2.line(img1, tuple(cursor), tuple([15,15]), (255,0,0), 2)

plt.figure()
plt.imshow(img1)

#%%
## Keypoint descriptor

# compute the gradient's magnitude as well as their orientation. Note that
# this time we make use of atan
gradNorm = (gxPatch**2+gyPatch**2)**0.5
gradOrient = np.arctan2(gyPatch, gxPatch)

# divide the range [-pi,pi)to 8 segments
binsize = 2*np.pi/8
bin = np.arange(-np.pi, np.pi, binsize)

# weight the orientation
weights = np.zeros(len(bin))
for i in range(len(bin)-1):
    weights[i] = np.sum(np.sum(gradNorm[(gradOrient>=bin[i]-binsize/2) & (gradOrient<bin[i]+binsize/2)]))
# weights[0] += np.sum(np.sum(gradNorm[gradOrient>=bin[-1]+binsize/2]));
weights = weights/weights.max() # normalise it

# visualise the weights over the orientations
X = np.zeros(len(weights))
Y = X
scaledWeights = 1-np.exp(-weights)
plt.figure()
# scaledWeights * np.cos(bin) is element-wise multiplication
plt.subplot(1,2,1), plt.quiver(X, Y, scaledWeights*np.cos(bin), -scaledWeights*np.sin(bin), scale=1)
plt.axis('scaled')

# You can also view the weights as a barchart
# plt.figure()
objects = ('-pi','-pi*3/4','-pi/2','-pi/4','0','pi/4','pi/2','pi*3/4','pi')
y_pos = np.arange(len(weights))
plt.subplot(1,2,2)
plt.bar(y_pos, weights, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Weights')
plt.title('Histogram')

#%%
## Using OpenCV built-in SIFT function
sift = cv2.xfeatures2d.SIFT_create()
kp,des = sift.detectAndCompute(gray, None)
imgSift = img.copy()
imgSift=cv2.drawKeypoints(gray,kp,imgSift,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.figure()
plt.imshow(imgSift)




plt.show()

# %%