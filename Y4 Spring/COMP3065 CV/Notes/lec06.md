# lec06: Camera Modeling

[toc]

## Projection

- A **camera model** is a function which **maps 3-dimensional world** onto a **2-dimensional plane**, called the **image plane**.
- There are many camera models of varying complexity, and a natural dividing line which helps categorize them is whether or not they are able to **capture perspective**.
    - **Perspective(Pinhole) Camera**: Perspective, or the perspective effect is simply the property that objects far away from us appear smaller than objects up close.
    - **Orthographic Camera**: Cameras Which Do Not Capture The Perspective Effect

### Pinhole Projection

<img src="./assets/截屏2025-04-03 12.31.07.png" alt="截屏2025-04-03 12.31.07" style="zoom:50%;" />

- Camera system can be designed by **placing a barrier** with a small aperture between the 3D object and a photographic film or sensor.
- A pinhole camera is a **simple camera without a lens** but with a tiny aperture (the so-called pinhole)—effectively a light-proof box with a small hole in one side.
- Each point on the 3D object emits multiple rays of light outwards.
    - Without a barrier, every point on the film will be influenced by light rays emitted from every point on the 3D object.
    - Due to the barrier, **only one (or a few) of these rays** of light passes through the aperture and hits the film.



**Camera Modeling: A formal construction of the pinhole camera model (perspective projection)**

- The film is commonly called the **image or retinal plane**:
    - The 2D plane where the projection of the 3D scene is captured, forming the image.
- The **aperture** is referred to as the **pinhole O** or **center of the camera**.
    - The point through which all light rays from the 3D scene pass.
- **The focal length f**.
    - The distance between the image plane and the pinhole O.
- Camera Intrinsic
    - Parameters such as focal length, principal point (the intersection of the optical axis with the image plane), and skew (if the image axes are not perpendicular).

<img src="./assets/截屏2025-04-03 13.23.22.png" alt="截屏2025-04-03 13.23.22" style="zoom:50%;" />

**The effect of varying aperture size?**

- As the aperture size increases, the number of light rays that passes through the barrier consequently increases.
- Then each point on the film may be affected by light rays from multiple points in 3D space, **blurring the image.**
- A smaller aperture size causes less light rays to pass through, resulting in crisper but darker images.

<img src="./assets/截屏2025-04-03 13.30.18.png" alt="截屏2025-04-03 13.30.18" style="zoom:50%;" />

### Orthographic Projection

- The projection rays are now **perpendicular to the retinal plane**. As a result, this model **ignores depth** altogether.
- Can be achieved using specialized hardware (e.g., telecentric lenses) or simulated in software.
- Orthographic cameras are particularly useful in technical and scientific applications where preserving accurate scale and proportions is essential.

<img src="./assets/截屏2025-04-03 13.28.59.png" alt="截屏2025-04-03 13.28.59" style="zoom:50%;" />

## Cameras and Lenses

- **透镜作用**：透镜通过聚焦光线，折射光线使其汇聚于成像平面，从而形成清晰明亮的图像。
- **焦点**：所有平行光轴的光线被透镜聚焦于一个点，称为焦点。
- **焦距**：焦点到透镜光学中心的距离称为焦距。

### Properties of lenses

- 平行于光轴的光线**会聚焦到焦点**。
- 通过透镜光学中心的光线不会偏折，继续沿直线传播。
- 来自三维世界中某点P的所有光线会被透镜折射，汇聚到成像平面上的单点P′（如果P在焦点上）

<img src="./assets/截屏2025-04-03 13.32.45.png" alt="截屏2025-04-03 13.32.45" style="zoom:50%;" />

### Problems with lenses

- **焦点**：透镜只能完美聚焦位于特定距离（焦平面）上的光线，焦点上的物体在图像中清晰，其他距离的物体则形成模糊的圆圈（焦散圆），导致图像模糊
- **景深**：物体在一定距离范围内清晰可见的范围叫做景深。
    - 景深受光圈大小、焦距和拍摄距离等因素影响。
    - **浅景深**：只有窄范围的距离清晰，适用于通过大光圈、长焦距和近距离拍摄来隔离背景。
    - **深景深**：较宽范围的距离清晰，适用于通过小光圈、广角镜头和远距离拍摄来保持整个场景清晰。

- The focal length determines the lens's **field of view and magnification**:
    - A shorter focal length provides a wider field of view.
    - A longer focal length provides a narrower field of view (zoom).

- We thus can arrive at a similar construction to the pinhole model that relates a point P in 3D space with its corresponding point P’ in the image plane

<img src="./assets/截屏2025-04-03 15.30.53.png" alt="截屏2025-04-03 15.30.53" style="zoom:50%;" />

### Paraxial refraction model 平行轴折射模型

- **透镜的推导**：采用了平行轴（或“薄透镜”）假设，称为平行轴折射模型。
- **平行轴折射模型**：基于薄透镜假设，可能会产生一些像差。
    - **径向畸变**：随着距离光轴的远近，图像的放大率增大或减小。
    - **枕形畸变**：放大率增大。
    - **桶形畸变**：放大率减小。

## Perspective Projection Properties

- **Many-to-One Mapping**
    - 多个三维空间中的点可以映射到二维投影中的同一点，这是因为透视投影将三维世界“压平”到二维平面，丧失了深度信息。
- **Scaling/Foreshortening**
    - 距离物体的远近与其图像大小成反比。
    - 当一条线（或表面）与图像平面平行时，透视投影的效果是**缩放**。
    - 当一条线（或表面）不平行于图像平面时，使用“**变短**”来描述投影畸变（即，沿光轴方向的维度相对于前向维度被压缩

<img src="./assets/截屏2025-04-03 15.39.02.png" alt="截屏2025-04-03 15.39.02" style="zoom:50%;" />

- **Lines, distances, angles 线、距离、角度**：
    - 三维空间中的线投影为二维空间中的线。
    - 距离和角度不被保持。
    - 平行线通常不会投影为平行线（除非它们平行于图像平面）。
- **Vanishing points:**
    - 每组平行线（=方向）在不同的点相交。该方向的消失点即为该点。
    - 同一平面上的平行线集会导致共线的消失点。
    - 该线称为该平面的地平线。

<img src="./assets/截屏2025-04-03 15.43.00.png" alt="截屏2025-04-03 15.43.00" style="zoom:50%;" />

## Properties of Orthographic Projection

- Parallel lines project to parallel lines.
- Size does not change with distance from the camera.

## Going to digital image space

**Geometric Camera Modeling**

- **Intrinsic parameters**: Define the camera's internal geometry
- **Extrinsic parameters**: Define the camera's position and orientation in the world.

**3D to 2D Mapping**

- A point P in 3D space mapped (or projected) into a 2D point P' in the image plane
- This $R^3 \to R^2$ mapping is referred to as a **projective transformation.**

<img src="./assets/截屏2025-04-03 19.34.48.png" alt="截屏2025-04-03 19.34.48" style="zoom:50%;" />

- This projection of 3D points into the image plane **does not directly correspond** to what we see in actual digital images for the following reasons.

    - Points in the digital images are in a **different reference** system than those in the **image plane**.
    - Digital images are divided into **discrete pixels**, whereas points in the image plane are **continuous**.

## The Camera Matrix Model and Homogeneous Coordinates



## Camera Calibration

- Capture an image of an object with known geometry.
- Identify correspondences between 3D scene points and image points
- Use the formula to calculate both intrinsic and extrinsic parameter
