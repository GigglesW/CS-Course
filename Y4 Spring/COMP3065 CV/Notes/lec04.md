# lec04: Image Stitching 1

[toc]

## Geometric Transformation

In a geometric transformation each point `(x, y)` of image A is **mapped** to a point `(u, v)` in a new coordinate system

- **Translation** 平移
- **Rotation** 旋转
- **Scale** 缩放
- **Euclidean transform** = translation + rotation
- **Similarity transform** = translation + rotation + scale
- **Aspect Ratio** 调整长宽比
- **Shear** 
- **Affine transform 仿射变换** = translation + rotation + scale + aspect ratio +shear
    - Origin does not necessarily map to origin
    - **Lines** map to **lines**, **Parallel lines** map to **parallel lines**
    - Ratios (lengths and areas) are **preserved**
    - Compositions of affine transforms are also affine transforms
- **Projective Geometry 投影**
    - Origin does not necessarily map to origin
    - Lines map to lines
    - Parallel lines **do not necessarily map** to parallel lines
    - Ratios (lengths and areas) are **not necessarily preserved**
    - Compositions of projective transforms are also projective transforms

<img src="./assets/截屏2025-03-26 13.04.43.png" alt="截屏2025-03-26 13.04.43" style="zoom:50%;" />

## Image Stitching

**The idea of Image Stitching**

1. Take a sequence of images from the same position.

    - Rotate the camera about its optical center, (more accurate with camera mounted on a tripod).

    - No tripods? Hold the camera and turn the body without changing the position.

2. To stitch two images: compute **transformation** between second image and first.

    - Extract interest points

    - Find Matches

    - Compute transformation

<img src="./assets/截屏2025-03-26 13.12.21.png" alt="截屏2025-03-26 13.12.21" style="zoom:50%;" />

3. Shift image to overlap
4. Blend together to create mosaic.
5. Repeat for all images

## Compute Transformation

- Extract feature points (e.g. SIFT)
- Find good matches (e.g. compare feature vectors)
- Compute Transformation

### Finding the Transformation

- Translation = 2 degrees of freedom
- Similarity = 4 degrees of freedom
- Affine = 6 degrees of freedom
- Projective (Homography) = 8 degrees of freedom
- ==这里的degree of freedom 理解为变量的数量==

### Least Square Formulation

- For each point $(x_i, y_i)$

$$
x_i+x_t=x'_i \quad y_i+y_t=y'_i \quad
$$

- We define the **residuals** as 

$$
r_{x_i}(x_t) = (x_i+x_t)- x'_i \\
r_{y_i}(y_t) = (y_i+y_t)- y'_i \\
$$

- **Goal: minimize sume of squared residuals**

$$
C(x_t,y_t)=\sum_{i=1}^n (r_{x_i}(x_t)^2 + r_{y_i}(y_t)^2)
$$

### Affine Transformation

<img src="./assets/截屏2025-03-26 13.34.35.png" alt="截屏2025-03-26 13.34.35" style="zoom:50%;" />

- 6 unknowns, **We need at least 6 equations, so 3 matches.**

- **Residuals**

<img src="./assets/截屏2025-03-26 13.35.28.png" alt="截屏2025-03-26 13.35.28" style="zoom:50%;" />

- **Cost function:**

<img src="./assets/截屏2025-03-26 13.35.45.png" alt="截屏2025-03-26 13.35.45" style="zoom:50%;" />

- **Matrix form**

<img src="./assets/截屏2025-03-26 13.39.00.png" alt="截屏2025-03-26 13.39.00" style="zoom:50%;" />

- For an **affine transform**, we have equations of the form $Ax_i+ b = y_i$ , solvable by linear regression.
- For the homography, the equation is of the form $H \tilde{x}_i \sim \tilde{y}_i$ (homogeneous coordinates) and the `~` means **it holds only up to scale**. 
- **The affine solution does not hold.**

## RANSAC

**RAndom SAmple Consensus**

- RANSAC loop for estimating homography:
    - Select four feature pairs (at random)
    - Compute **homography** H (exact)
    - Compute **inliers**
- **Keep the largest set of inliers**
- Re-compute least-squares H estimate using all of the inliers

<img src="./assets/截屏2025-03-26 13.46.15.png" alt="截屏2025-03-26 13.46.15" style="zoom:50%;" />











