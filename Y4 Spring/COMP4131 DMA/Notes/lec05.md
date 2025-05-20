# lec05: Unsupervised Learning

[toc]

## Introduction to Unsupervised Learning

**Supervised vs. Unsupervised Learning**

| Aspect   | Supervised Learning        | Unsupervised Learning               |
| -------- | -------------------------- | ----------------------------------- |
| Data     | Labeled                    | Unlabeled                           |
| Goal     | Predict outcomes           | Discover patterns                   |
| Examples | Classification, Regression | Clustering, ReductionDimensionality |

**Types of Unsupervised Learning**

- **Clustering**: Grouping similar data points (e.g., K-Means, Hierarchical Clustering).
- **Dimensionality Reduction**: Reducing the number of features (e.g., PCA, t-SNE).
- **Association Rule Learning**: Discovering relationships between variables (e.g., Apriori Algorithm).

## Clustering

### Definition of Clustering

- **Definition**: Grouping similar data points together based on their features.
- **Intuition:**
    - Unsupervised learning technique.
    - No predefined labels; the algorithm identifies natural groupings. 
    - Used for exploratory data analysis and pattern discovery.

**Types of Clustering**

- **Partitional Clustering**: Divides data into non-overlapping subsets (e.g., K-Means).
- **Hierarchical Clustering**: Builds a tree of clusters (e.g., Agglomerative, Divisive).
- **Density-Based Clustering**: Groups data based on density (e.g., DBSCAN).
- **Model-Based Clustering**: Assumes data is generated from a mixture of distributions (e.g., Gaussian Mixture Models).

### K-Means Clustering

- **Definition**: A type of unsupervised learning used for unlabeled data.
- **Goal**: Find groups in the data, with the number of groups represented by K.
- **Algorithm**:
    - Works iteratively to assign each data point to one of K groups. 
    - Clusters data points based on feature similarity.
- **Results**:
    - Centroids of the K clusters (used to label new data).
    - Labels for the training data (each point assigned to a single cluster).

**Algorithm Steps**

- **Initialization**: Randomly initialize k cluster centroid
- **Assignment Step**: Assign each data point `x_j` to the nearest centroid
- **Update Step**: Recompute the centroids as the mean of all points assigned to each cluster:
- **Repeat**: Repeat the assignment and update steps until convergence (i.e., when the centroids no longer change significantly or a maximum number of iterations is reached).

**Limitations of K-Means**

- Sensitive to **initial centroid** positions.
- Requires the number of clusters to be specified in advance. 
- Struggles with non-spherical clusters and outliers.
- Not suitable for clusters of varying densities.

**Choosing the Righ Number of Clusters**

- **Elbow Method**: Plot the sum of squared errors (SSE) vs. the number of clusters and look for the ”elbow” point.
- **Silhouette Score**: Measures how similar a data point is to its own cluster compared to other clusters (range: -1 to 1).

> **肘部法则的思路**
>
> - 随着 `k` 值的增加，`inertia` 会持续减少，因为更多的簇意味着每个簇的样本点会更接近其中心。
> - 然而，`inertia` 的下降幅度会在某个 `k` 值处明显放缓。这个拐点被称为“**肘部点 (Elbow Point)**”。
> - **该拐点对应的 `k` 通常是最佳聚类数**

<img src="./assets/截屏2025-03-17 16.23.22.png" alt="截屏2025-03-17 16.23.22" style="zoom:50%;" />

**Hard vs Soft Assignments**

- In K-means, there is a hard assignment of feature vectors to a cluster. However, for feature vectors **near the boundary** this may be a poor representation.
- To address these problems, we use **soft clustering** - **Gaussian Mixture Model**.
- Soft clustering is a form of clustering where **observations may belong to multiple clusters**.

### Gaussian Mixture Model (GMM)

**Multivariate Gaussians**

- For `d` dimensions, the Gaussian distribution of a vector $x=(x_1, x_2, \dots, x_d)^T$ is defined by:
    - $\mu$: Mean vector of the Gaussian
    - $\Sigma$: Covariance matrix of the Gaussian

<img src="./assets/截屏2025-03-17 13.55.26.png" alt="截屏2025-03-17 13.55.26" style="zoom:50%;" />

**Gaussian Mixture Model**

- GMM is a **probabilistic model** for clustering based on Gaussian distributions.
- Unlike K-Means, it **assigns a probability** to each data point belonging to every clusters.
- Uses the **Expectation-Maximization (EM)** algorithm for parameter estimation.
- **Key Concepts:**
    - Each cluster is represented by a **Gaussian distribution**.
    - The algorithm estimates the parameters of these distributions.

**Expectation-Maximizaition (EM) Algorithm**

- Initialize Gaussian parameters (means, variances, weights). 
- **Expectation Step (E-Step)**: Compute probabilities for each data point. 
- **Maximization Step (M-Step)**: Update parameters to maximize likelihood.
- Repeat until convergence.

**Defining a stopping criterion:**

- With k-means clustering, we iteratively recalculated means and reassigned observations until convergence, **where observations stopped moving between clusters**.
- However, since we’re now dealing with soft clustering that involves continuous probabilities, we can’t rely on this same type of convergence.
- Instead, we’ll set a stopping criterion to end the iterative cycle. The cycle will stop once the observation probabilities **stop changing by more than some threshold.**

## Dimensionality Reduction

**Curse of Dimensionality**

- As the number of dimensions increases, data becomes sparse, and distance metrics lose meaning.
- **Examples:**
    - High computational cost.
    - Overfitting in machine learning models. 
    - Diﬀiculty in visualizing and interpreting data.

**What is Dimensionality Reduction**

- **Definition**: A technique to reduce the number of features (dimensions) in a dataset while preserving its structure.
- **Motivation**:
    - Improves computational eﬀiciency.
    - Reduces noise and redundancy.
    - Enables visualization of high-dimensional data.

### Principal Component Analysis (PCA)

<img src="./assets/截屏2025-03-17 15.16.08.png" alt="截屏2025-03-17 15.16.08" style="zoom:50%;" />

**PCA Algorithms**

- **Standardize the Data**
    - Compute the mean of the dataset:
    - Center the data:
- **Compute the Covariance Matrix**
- **Compute the Eigenvalues and Eigenvectors**
- **Sort Eigenvectors by Eigenvalues**
    - Order eigenvectors by decreasing eigenvalues:
    - The eigenvectors corresponding to the largest eigenvalues capture the most variance.
- **Select the Top K Eigenvectors**
    - K is the number of principal components you choose to keep.
- **Project the Data onto the New Subspace**
    - Transform the data into the new K-dimensional subspace:
    - Z is the reduced representation of the original data.

**Limitations of PCAs**

- **Linearity Assumption**: PCA assumes linear relationships between variables.
- **Sensitivity to Scaling**: Requires standardized data.
- **Loss of Information**: May discard important variance in lower components.