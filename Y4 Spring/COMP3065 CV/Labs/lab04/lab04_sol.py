#%%
import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('uttower_left.jpg',0)
img2 = cv2.imread('uttower_right.jpg',0)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
matchesMask = mask.ravel().tolist()

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
plt.figure()
plt.imshow(img3, 'gray')
plt.xticks([]),plt.yticks([])
print('!!!')

w = img2.shape[1]
h = img2.shape[0]

offset_x = w//3*2
offset_y = h//3

dst_pts1 = dst_pts.copy()
dst_pts1[:,:,0] = dst_pts1[:,:,0]+offset_x
dst_pts1[:,:,1] = dst_pts1[:,:,1]+offset_y
MM, mask = cv2.findHomography(src_pts, dst_pts1, cv2.RANSAC,5.0)
img_final = cv2.warpPerspective(img1, MM, (w+offset_x, h+offset_y))

for i in range(h):
    for j in range(w):
        if img_final[i+offset_y][j+offset_x]==0:
            img_final[i+offset_y][j+offset_x] = img2[i][j]
        elif img2[i][j]!=0:
            img_final[i+offset_y][j+offset_x] = img_final[i+offset_y][j+offset_x]/2+img2[i][j]/2

print('done stitching')
plt.figure()
plt.imshow(img_final,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.show()



# %%