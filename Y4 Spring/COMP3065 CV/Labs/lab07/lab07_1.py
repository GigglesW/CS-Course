#%%
import cv2
import numpy as np

# Load the left and right images
imgLeft = cv2.imread("img/left.png", cv2.IMREAD_GRAYSCALE)
imgRight = cv2.imread("img/right.png", cv2.IMREAD_GRAYSCALE)

# Check if images have the same size
if imgLeft.shape != imgRight.shape:
    raise ValueError("Images have different sizes")

# Set parameters
disparityMax = 64  # Max disparity value
windowSize = 3  # Search window size

# Initialize disparity map
disparityMap = np.zeros_like(imgLeft, dtype=np.float32)

# Get half window size
h = windowSize // 2


### your code here. Good luck:)


##show result


# Normalize disparity map
disparityMap_display = disparityMap / np.max(disparityMap)


# Convert disparity map to uint8
disparityMap_display_uint8 = (disparityMap_display * 255).astype(np.uint8)

# Convert the disparity map to a colored image
disparityMap_colored = cv2.applyColorMap(disparityMap_display_uint8, cv2.COLORMAP_JET)

# Write colored disparity map image to file
cv2.imwrite("disparity_map_colored.png", disparityMap_colored)


# Display disparity map
cv2.imshow("Disparity Map", disparityMap_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()