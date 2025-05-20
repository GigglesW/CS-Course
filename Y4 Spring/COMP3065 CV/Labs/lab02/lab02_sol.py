#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d

img = cv2.imread('skull.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numFilters = 5
sigma = 0.5 #the base scale of the gaussians, you can change this to see its effect
H = np.zeros([9,9,numFilters])
imgFiltered = np.zeros(img.shape+(numFilters,))
imgDoG = np.zeros(img.shape+(numFilters-1,))

for i in range(numFilters):
    k = cv2.getGaussianKernel(9, sigma)
    H[:,:,i] = k * np.transpose(k)
    # Convolve the gaussfilter with the origianl image
    imgFiltered[:,:,i] = cv2.filter2D(img, cv2.CV_64F, H[:,:,i])
    sigma = sigma*4

fig = plt.figure()
for i in range(numFilters):
    X, Y = np.meshgrid(np.linspace(0, 8, num=9), np.linspace(0, 8, num=9))
    plt.subplot(1,numFilters,i+1)
    plt.title(i)
    #ax = fig.gca(projection='3d')
    ax = fig.add_subplot(1, numFilters, i+1, projection='3d')
    surf = ax.plot_surface(X, Y, H[:,:,i], cmap='jet', shade=False)


for i in range(numFilters-1):
    imgDoG[:,:,i] = imgFiltered[:,:,i]-imgFiltered[:,:,i+1];


plt.figure()
for i in range(numFilters-1):
    plt.subplot(1,numFilters-1,i+1), plt.imshow(imgDoG[:,:,i],cmap='gray')
    plt.xticks([]),plt.yticks([])

#%%
## Keypoint localization
patchsize = 5
errors = np.zeros(img.shape) # to store the smaller eigen value of image patches
directionU = np.zeros(img.shape) # to store the x component of the direction of an image patch
directionV = np.zeros(img.shape) # to store the y component of the direction of an image patch

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
plt.figure()
plt.subplot(1,2,1), plt.imshow(sobelx, cmap='gray')
plt.subplot(1,2,2), plt.imshow(sobely, cmap='gray')

for i in range(patchsize//2, img.shape[0] - patchsize//2):
    for j in range(patchsize//2, img.shape[1] - patchsize//2):
        # Compute the Hessian of this image patch
        sumIx = sobelx[i-patchsize//2:i+patchsize//2+1, j-patchsize//2:j+patchsize//2+1].mean()
        sumIy = sobely[i-patchsize//2:i+patchsize//2+1, j-patchsize//2:j+patchsize//2+1].mean()

        patchHessian = np.array([[sumIx**2, sumIx*sumIy], [sumIx*sumIy, sumIy**2]])

        error, direction = np.linalg.eig(patchHessian)
        errors[i, j] = error.min()
        directionU[i, j] = direction[:, np.argsort(error)][0,0]
        directionV[i, j] = direction[:, np.argsort(error)][1,0]
        # The normalized (unit “length”) eigenvectors, such that the column v[:,i] is the eigenvector corresponding to the eigenvalue w[i].

plt.figure()
plt.imshow(errors, cmap='gray')

#%%
[X, Y] = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))
U = np.zeros(X.shape)
V = np.zeros(X.shape)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        U[i,j] = directionU[img.shape[0]-Y[i,j]-1,X[i,j]]
        V[i,j] = -directionV[img.shape[0]-Y[i,j]-1,X[i,j]]
# for better visualisation, we only display the directions at every n
# points along both x and y axises.
n = 7
plt.figure()
#plt.quiver(X, Y, U, V, units='height')
plt.quiver(X[::n, ::n], Y[::n, ::n], U[::n, ::n], V[::n, ::n])
plt.axis('scaled')

plt.show()


# %%