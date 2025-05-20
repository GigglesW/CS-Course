#%%
import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0), ..., (6,5,0)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# print(f'objp = {objp}')

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

# Specify the directory path
directory_path = 'chessboard'

# List all files in the directory
image_files = [f for f in os.listdir(directory_path) if f.endswith('.jpg')]

for fname in image_files:
    # Construct the full file path
    file_path = os.path.join(directory_path, fname)
    
    # Read the image
    img = cv.imread(file_path)
    
    if img is None:
        print(f"Error: Unable to read image {file_path}")
        continue
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7, 6), None)
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        # 用于进一步优化角点位置，从而提高精度
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (7, 6), corners2, ret)
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        plt.figure(figsize=(6, 6))
        plt.imshow(img_rgb)
        plt.title(f'Chessboard corners: {fname}')
        plt.axis('off')


#%%
# Calibrate camera
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print results
print("Camera matrix :\n", mtx)
print("Distortion coefficients :\n", dist)

#%%
# Undistort an image
img = cv.imread('./chessboard/left12.jpg')  # test image
h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# Undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# Crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]

cv.imwrite('calibresult.png', dst)

# Display undistorted image
img_dst = cv.imread('calibresult.png')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
dst_rgb = cv.cvtColor(img_dst, cv.COLOR_BGR2RGB)

# 创建图像对比展示
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dst_rgb)
plt.title('Undistorted')
plt.axis('off')

# %%
