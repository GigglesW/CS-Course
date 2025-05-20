#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('skull.jpg', cv2.IMREAD_GRAYSCALE)

# 使用Sobel算子计算梯度
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 定义补丁的中心位置和大小
cursor = np.array([30, 40])
patchsize = 15


#%%