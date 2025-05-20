import cv2 
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('skull.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#################### Task 1 ####################
def applySobelAuto():
    # 用sobel算子在水平和垂直方向进行边缘检测
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

    plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original'), plt.xticks([]), plt.yticks([]) 

    plt.subplot(2,2,2),plt.imshow(gray,cmap = 'gray') 
    plt.title('Gray'), plt.xticks([]), plt.yticks([]) 

    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray') 
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([]) 

    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray') 
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

def applyKernel(image, kernel):
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2

    # 使用 0 填充图像边界
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    output = np.zeros_like(image, dtype=float)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+k_h, j:j+k_w]
            output[i, j] = np.sum(region * kernel)
    return output

def applySobelManual():
    kernel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    sobel_x_manual = applyKernel(gray, kernel_x)
    sobel_y_manual = applyKernel(gray, kernel_y)

    sobel_x_auto = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sobel_y_auto = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

    plt.subplot(2,2,1),plt.imshow(sobel_x_auto,cmap = 'gray') 
    plt.title('Sobel X Auto'), plt.xticks([]), plt.yticks([]) 

    plt.subplot(2,2,2),plt.imshow(sobel_y_auto,cmap = 'gray') 
    plt.title('Sobel Y Auto'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,3),plt.imshow(sobel_x_manual,cmap = 'gray') 
    plt.title('Sobel X Manual'), plt.xticks([]), plt.yticks([]) 

    plt.subplot(2,2,4),plt.imshow(sobel_y_manual,cmap = 'gray') 
    plt.title('Sobel Y Manual'), plt.xticks([]), plt.yticks([])

    plt.show()

#################### Task 2 ####################
def magnitude_orientation():
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

    mag = np.sqrt(sobelx ** 2, sobely ** 2)
    mag_norm = (mag / mag.max() * 255).astype(np.uint8)     # normalization

    ori = np.arctan2(sobely, sobelx)                #  [-pi, pi)
    ori_degrees = (np.degrees(ori) + 360) % 360     # 映射到 [0,360)

    h, w = ori_degrees.shape
    ori_color = np.zeros((h, w, 3), dtype=np.uint8)

    # 定义不同区间的掩码
    mask_red = (ori_degrees >= 0) & (ori_degrees < 90)
    mask_cyan = (ori_degrees >= 90) & (ori_degrees < 180)
    mask_green = (ori_degrees >= 180) & (ori_degrees < 270)
    mask_yellow = (ori_degrees >= 270) & (ori_degrees < 360)

    # 为对应区间赋予颜色（RGB 顺序）
    ori_color[mask_red] = [255, 0, 0]       # 红色：0-90°
    ori_color[mask_cyan] = [0, 255, 255]    # 青色：90-180°
    ori_color[mask_green] = [0, 255, 0]     # 绿色：180-270°
    ori_color[mask_yellow] = [255, 255, 0]  # 黄色：270-360°

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(mag_norm, cmap='gray')
    plt.title("Gradient Magnitude")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(ori_color)
    plt.title("Gradient Orientation (Color Coded)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    # applySobelAuto()
    # applySobelManual()
    magnitude_orientation()




if __name__ == '__main__':
    main()