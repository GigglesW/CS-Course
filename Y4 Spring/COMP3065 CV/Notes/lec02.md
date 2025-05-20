# lec02: Describing Image Regions and Patches

[toc]

## Image

- **Image is a matrix of intensity values**
- **Segments** (irregular) or rectangular **image patches** are widely used in computer vision tasks.

## Common features used in CV

- We need to define a set of **descriptive features** and concatenate them to produce a feature vector
- We should choose features that reflect the relevant properties of the viewed object, such as **color features, texture features, shape features, etc.**

**Colour Features**

- Colour correlates well with class identity.
- **Histograms**
    - Are invariant to translation and rotation.
    - Change slowly as viewing direction changes.
    - Change slowly with object size.
    - Change slowly with occlusion.

**Texture Features**

- Colour is **a property of a single pixel**, texture features capture **the frequency** with which patterns of colour/grey level appear.
    - e.g. Local Binary Patterns (LBP)

<img src="./assets/截屏2025-03-17 22.44.47.png" alt="截屏2025-03-17 22.44.47" style="zoom:50%;" />

**LBP Feature Vector**

- Divide the patch into cells e.g. 16 x 16 pixels per cell.
- Compute the local patch description number of each pixel.
- Histogram these numbers over each cell.
- Optionally normalize each histogram (so its bins sum to 1).
- Concatenate (normalized) histograms to make the feature vector.

**Shape Features**

- Focus on **image gradient** measures:
    - The gradient of an image measures how it is changing.
    - The boundaries of objects are often associated with large gradients.
    - Distributions of gradients and **gradient orientations** reflect boundary shape (and internal boundaries between parts, surfaces, etc.).

## Techniques

- Edge Detection
- An edge is a place of **rapid change** in the image intensity function

<img src="./assets/截屏2025-03-17 22.55.20.png" alt="截屏2025-03-17 22.55.20" style="zoom:50%;" />

- **Image Gradient: Example**

<img src="./assets/截屏2025-03-17 22.58.27.png" alt="截屏2025-03-17 22.58.27" style="zoom:50%;" />

- **Image Transformations**

<img src="./assets/截屏2025-03-17 23.00.16.png" alt="截屏2025-03-17 23.00.16" style="zoom:50%;" />

- **Image Filtering**
    - Replace each pixel by a **linear combination** of its neighbors
    - The prescription for the linear combination is called the “kernel” (or “mask”, “filter”)

<img src="./assets/截屏2025-03-17 23.01.11.png" alt="截屏2025-03-17 23.01.11" style="zoom:50%;" />

- **Spatial Filtering: Convolution**
    - Many filters follow a similar pattern - multiplying each image value by a corresponding filter entry, and summing the results.

- **Derivative Filters**
    - **Sobel Operators**: Applied separately and results combined to estimate overall gradient magnitude.

<img src="./assets/截屏2025-03-17 23.02.42.png" alt="截屏2025-03-17 23.02.42" style="zoom:50%;" />

- **Alternative derivative filters**

<img src="./assets/截屏2025-03-17 23.05.40.png" alt="截屏2025-03-17 23.05.40" style="zoom:50%;" />

## Histogram of Oriented Gradients (HoG)

- **Basic idea:**
    - Local shape information often well described by the **distribution of intensity gradients** or edge directions
    - Convert the image (width*height*channels) into **a feature vector**, then apply the classification algorithms
    - The intent is to generalize the object in such a way that the **same object** (e.g., person) produces **as close as possible** to the same feature descriptor when viewed under different conditions
- **Algorithms**
    - Divide the patch into small cells.
    - Define slightly larger blocks, covering several cells.
    - Compute **gradient magnitude and orientation** at each pixel.
    - Compute a local weighted histogram of gradient orientations for each cell, weighting by some function of magnitude.
    - Concatenate histogram entries to form a HoG vector for each block.
    - Normalize vector values by dividing by some function of vector length.







