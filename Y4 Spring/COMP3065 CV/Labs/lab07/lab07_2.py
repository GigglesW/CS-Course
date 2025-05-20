import cv2
import numpy as np

# Load the two images
img1 = cv2.imread('./Lab6_I/warrior0.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./Lab6_I/warrior1.png', cv2.IMREAD_GRAYSCALE)

# Feature matching using SIFT
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# Match features and compute fundamental matrix
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

pts1 = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
pts2 = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]

# Compute epipolar lines
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1, 1, 2), 2, F).reshape(-1, 3)

# Visualize epipolar lines and matching points
np.random.seed(0)
h, w = img1.shape

imgColor1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
imgColor2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

for r1, pt2 in zip(lines1, pts2):
    color = tuple(np.random.randint(0, 255, 3).tolist())
    x0, y0 = map(int, [0, -r1[2] / r1[1]])
    x1, y1 = map(int, [w, -(r1[2] + r1[0] * w) / r1[1]])
    imgColor1 = cv2.line(imgColor1, (x0, y0), (x1, y1), color, 5)
    # Convert pt2 to tuple of integers
    pt2 = (int(pt2[0][0]), int(pt2[0][1]))
    imgColor2 = cv2.circle(imgColor2, pt2, 15, color, -1)

#save image
cv2.imwrite("img1_eppl.png", imgColor1)
cv2.imwrite("img2_cir.png", imgColor2)

# Display the images
cv2.imshow('Image 1 with Epipolar Lines', imgColor1)
cv2.imshow('Image 2 with Matching Points', imgColor2)
cv2.waitKey(0)
cv2.destroyAllWindows()
