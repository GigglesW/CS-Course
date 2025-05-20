#%% 
# Overall Process
# SIFT 提取图像的关键点和描述符。
# 使用 kNN 找到每个描述符的 两个最近邻。
# 通过 Lowe 比率测试 筛选出有效匹配（好的匹配）。
# 使用 RANSAC 来计算Homography，并筛选出 内点 和 外点。

################# Find Keypoints ##################
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_left = cv2.imread('uttower_left.jpg', cv2.IMREAD_GRAYSCALE)
img_right = cv2.imread('uttower_right.jpg', cv2.IMREAD_GRAYSCALE)
# print(img_left.shape)     # (683, 1024)
# print(img_right.shape)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img_left, None)
kp2, des2 = sift.detectAndCompute(img_right, None)
# print(len(kp1), des1.shape)     # 5316 (5316, 128)
# print(len(kp2), des2.shape)     # 4195 (4195, 128)

kp_img1 = cv2.drawKeypoints(img_left, kp1, None)
kp_img2 = cv2.drawKeypoints(img_right, kp2, None)

plt.figure()
plt.subplot(1, 2, 1)  
plt.imshow(kp_img1)
plt.title('Keypoint Left')
plt.axis('off')

plt.subplot(1, 2, 2)  
plt.imshow(kp_img2)
plt.title('Keypoint Right')
plt.axis('off')

#%% 
################# Find Good Matching Point ##################

# 设置 FLANN 参数
FLANN_INDEX_KDTREE = 0      # 0: 线性搜索 小数据 1: KD树 大数量
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
print(f'Number of matches: {len(matches)}')     # 5316
# 对于每个 des1 中的描述符，FLANN 会找到它与 des2 中的两个最接近的描述符
# 因此 matches 的长度由 des1 决定

good_matches = []
for m, n in matches:
    if m.distance < 0.70 * n.distance:  # 采用 Lowe 的比率测试
        good_matches.append(m)

print(f'Number of good matches: {len(good_matches)}')

img_matches = cv2.drawMatches(img_left, kp1, img_right, kp2, good_matches, None, 
                              flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

img_matches_rgb = cv2.cvtColor(img_matches, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_matches_rgb)
plt.title('Good Matches')
plt.axis('off')

# %%
################# Find Inners using RANSAC ##################
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# 使用 RANSAC 计算 Homography Matrix
# 5.0 是 RANSAC 的阈值，表示允许的最大点的重投影误差（单位：像素）
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
matchesMask = mask.ravel().tolist()
# print(H.shape)            # (3,3)
# print(len(matchesMask))   # 1028  

draw_params = dict(matchColor = (0,255,0),      # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask,   # draw only inliers
                   flags = 2)

inliers = cv2.drawMatches(img_left, kp1, img_right, kp2, 
                       good_matches, None, **draw_params)
plt.figure()
plt.imshow(inliers, 'gray')
plt.axis('off')

# %%
################# Image Stitching ##################
# Let say we assume the width and height of 
#  the final image is 5/3 and 4/3 of the original image.
h, w = img_right.shape

offset_x = w//3*2
offset_y = h//3

# 平移右图
dst_pts1 = dst_pts.copy()
dst_pts1[:,:,0] = dst_pts1[:,:,0]+offset_x
dst_pts1[:,:,1] = dst_pts1[:,:,1]+offset_y

HH, mask = cv2.findHomography(src_pts, dst_pts1, cv2.RANSAC, 5.0)
img_final = cv2.warpPerspective(img_left, HH, (w+offset_x, h+offset_y))

for i in range(h):
    for j in range(w):
        # 对于没有重叠的区域（空白区域），直接填充右图的像素
        if img_final[i+offset_y][j+offset_x]==0:
            img_final[i+offset_y][j+offset_x] = img_right[i][j]

        # 对于重叠区域，使用 加权平均 的方法来平滑过渡
        elif img_right[i][j]!=0:
            img_final[i+offset_y][j+offset_x] = img_final[i+offset_y][j+offset_x]/2+img_right[i][j]/2

plt.figure()
plt.imshow(img_final,cmap='gray')
plt.axis('off')


# %%
