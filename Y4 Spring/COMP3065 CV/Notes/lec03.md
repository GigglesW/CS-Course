# lec03: Point Features: SIFT

[toc]

## SIFT

> SIFT的基本原理是从图像中提取一组具有良好辨识度的特征点，这些特征点具有以下几个重要性质：
>
> - **尺度不变性**：在不同的图像尺度下，这些特征点依然能够被检测出来。这意味着无论图像被放大或缩小，算法都能够识别出同样的特征。
> - **旋转不变性**：无论图像旋转多少角度，SIFT算法都能保持特征点的稳定性。
> - **局部特征**：SIFT特征点的描述符是局部的，可以帮助进行精确的匹配，即使图像中有一定的遮挡或部分失真。
> - **鲁棒性**：SIFT算法在光照变化、图像噪声等干扰下依然表现出较高的稳定性。

 **Scale Invariant Feature Transform**

- Transform image data into scale-invariant coordinates relative to local features.

- **Scale-space extrema detection** (for **scale** invariance)
    - Search over all scales and image locations
    - Detect points that are invariant to scale and orientation
- **Keypoint localization** (for **translation** invariance)
    - A model is fit to determine the location and scale. Keypoints are selected based on measures of their stability
- **Orientation assignment** (for **rotation/orientation** invariance)
    - Compute best orientation for each keypoint region
- **Keypoint descriptor** (for **illumination** invariance)
    - Use local image gradients at selected scale and rotation to describe each keypoint region

## Step1: Scale-space Extrema Detection

**Gaussian Filter**

<img src="./assets/截屏2025-03-25 22.13.38.png" alt="截屏2025-03-25 22.13.38" style="zoom:50%;" />

**Scale Invariance**

- Find points whose **surrounding patches** (at some scale) **are distinctive**.
- Gaussian masks have a **natural scale**.
- Larger values of `σ` produce greater blurring

<img src="./assets/截屏2025-03-25 22.20.58.png" alt="截屏2025-03-25 22.20.58" style="zoom:50%;" />

**Scale Spaces in SIFT**

- Scale space is separated into **octaves**
- In each octave, the initial image is repeatedly convolved with Gaussians to produce a set of scale space images
- Adjacent Gaussians are **subtracted** to produce the **DoG**
- Once a complete octave has been processed, the Gaussian image is resampled by taking every second pixel in each row and column to start the next level

**Summary**

- Several octaves of the original image are generated
- Each octave's image size is half of the previous one
- Within an octave, images are progressively blurred using the Gaussian Blur operator

## Step 2: Keypoint Localization

**Laplacian of Gaussian**

- It highlights regions of **rapid intensity change** and is therefore often used for **edge/corner/keypoint** detection
- The second order derivative is **extremely sensitive to noise**
    - The blur smooths it out the noise and stabilizes the second order derivative
- However, computationally intensive

**Difference of Gaussians**

- Calculate the difference between two **consecutive Gaussian** images
- These Difference of Gaussian images are **approximately equivalent to the Laplacian of Gaussian**

**Extrema Detection**

- Locate maxima/minima in DoG images
- A point is marked as a "**key point**" if it is **the greatest or least of all neighbors**
- The marked points are the approximate maxima/minima

**Getting Rid of Low Contrast Keypoints**

> 低于一定阈值的keypoint会被消除

- Some of the detected keypoints lie along an edge, or they don’t have enough contrast
    - In both cases, they are not as useful as features and should be **eliminated**
- If the DoG value at an extrema is **less than a threshold** (e.g 0.03), the keypoint is rejected

**Getting Rid of Edges**

<img src="./assets/截屏2025-03-25 22.33.25.png" alt="截屏2025-03-25 22.33.25" style="zoom:50%;" />

**SIFT: Eliminating Edge Responses**

- In SIFT, efficiency is increased by just **calculating the ratio of two eigenvalues**
- If the above ratio for a candidate keypoint is **larger than a threshold**, the keypoint is poorly localized and hence rejected
- Both extrema images go through the two tests: **the contrast test** and **the edge test**

**SIFT Step 2: Summary**

- Produce DoGs using two consecutive images in an octave for all octaves
- Detect the maxima/minima in the DoG images
- Reject the keypoints if they had **a low contrast** or if they were **located on an edge**

## Step 3: Orientation Assignment

**Orientation Estimation**

- Each keypoint should be characterized by location, scale, **orientation**
- Collect **gradient directions and magnitudes** around each keypoint
- Figure out the most **prominent orientation** in that region
- Assign this orientation to the keypoint
- Any later calculations are done relative to this orientation
    - This ensures rotation invariance

**SIFT Step 3: Summary**

- To assign an orientation we calculate the **gradient magnitude** and **direction of a small region** around the keypoint
- Using the histogram, the most prominent gradient orientation is identified
    - Peak of the histogram
- Assign it to the keypoint

## Step 4: SIFT Descriptor

- At this point, each keypoint has the **location, scale, orientation**
- Next is to compute a descriptor for the local image region(window) around each keypoint
- Region normalization
    - Rotate the window to standard orientation
    - Scale the window size based on the scale at which the point was found
- Take **16x16 square window** around detected keypoint.
- Compute edge orientation (angle of the gradient – 90 degree) for each pixel.
- Throw out weak edges (threshold gradient magnitude).
- Create histogram of surviving edge orientations.

<img src="./assets/截屏2025-03-25 22.39.39.png" alt="截屏2025-03-25 22.39.39" style="zoom:50%;" />

- Full version:
    - Divide the 16x16 window into a 4x4 grid of cells
    - Within the 4x4 cell, the orientations and gradient magnitudes are calculated
    - Put these orientations into an 8 bin histogram (the amount added to the bin depends on the magnitude of the gradient)

<img src="./assets/截屏2025-03-25 22.40.22.png" alt="截屏2025-03-25 22.40.22" style="zoom:50%;" />

**SIFT: Invariance Properties**

- To be robust to **intensity value changes**
    - Use gradient orientations
- To be **scale invariant**
    - Estimate the scale using scale space extrema detection
    - Calculate the gradient after Gaussian smoothing with this scale
- To be **orientation invariant**
    - Rotate the gradient orientations using the dominant orientation in a neighborhood
- To be **Illumination invariant**
    - Working in gradient space, so robust to I = I + b

