# %%
import cv2 
import numpy as np 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Load Image
img = cv2.imread('skull.jpg', cv2.IMREAD_GRAYSCALE)
print(f'Image shape: {img.shape}')      # (253,199)

numFilters = 5
sigma = 0.5

H = np.zeros((9, 9, numFilters))
imgFiltered = np.zeros(img.shape + (numFilters,))
imgDoG = np.zeros(img.shape + (numFilters - 1,))    # 计算相邻两个不同尺度的高斯滤波器的差异

# Apply Gaussian Filter
for i in range(numFilters):
    k = cv2.getGaussianKernel(9, sigma)     # 生成1维高斯核
    H[:, :, i] = np.outer(k, k)             # 用外积生成2维高斯核
    
    imgFiltered[:, :, i] = cv2.filter2D(img, cv2.CV_64F, H[:, :, i])
    sigma *= 4      # 更新高斯核的sigma值

fig = plt.figure()
for i in range(numFilters):
    X, Y = np.meshgrid(np.linspace(0, 8, num=9), np.linspace(0, 8, num=9))
    plt.subplot(1, numFilters, i+1)
    plt.title(i)

    ax = fig.add_subplot(1, numFilters, i+1, projection='3d')
    surf = ax.plot_surface(X, Y, H[:,:,i], cmap='jet', shade=False)

# Calculate DoG
for i in range(numFilters - 1):
    imgDoG[:,:,i] = imgFiltered[:,:,i] - imgFiltered[:, :, i+1]

plt.figure()
for i in range(numFilters - 1):
    plt.subplot(1, numFilters - 1, i + 1)
    plt.imshow(imgDoG[:,:,i], cmap='gray')
    plt.xticks([]), plt.yticks([])


# %% 
# Keypoint Localization

# Sobel Filter
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

plt.figure()
plt.subplot(1,2,1), plt.imshow(sobelx, cmap='gray')
plt.subplot(1,2,2), plt.imshow(sobely, cmap='gray')

# 使用 OpenCV cornerEigenValsAndVecs 计算特征值和特征向量
hessian_output = cv2.cornerEigenValsAndVecs(img, blockSize=5, ksize=3)
print(hessian_output.shape)     # (253, 199, 6)
# hessian_output[..., 0] -> 最大特征值
# hessian_output[..., 1] -> 最小特征值
# hessian_output[..., 2:4] -> 第一个特征向量的 x 和 y 分量
# hessian_output[..., 4:6] -> 第二个特征向量的 x 和 y 分量

errors = hessian_output[..., 1] # 提取最小特征值
directionU = hessian_output[..., 4]
directionV = hessian_output[..., 5]

plt.figure()
plt.imshow(errors, cmap='gray')
plt.title("Minimum Eigenvalue (Curvature)")
plt.colorbar()
plt.show()


# %%
[X, Y] = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))

# 使用 NumPy 高效替代循环
U = directionU[img.shape[0] - Y - 1, X]
V = -directionV[img.shape[0] - Y - 1, X]

# 画箭头图
n = 7       # 每格7个像素画一个箭头
plt.figure()
plt.quiver(X[::n, ::n], Y[::n, ::n], U[::n, ::n], V[::n, ::n])
plt.axis('scaled')
plt.show()

# %%