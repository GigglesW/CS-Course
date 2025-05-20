# lec06: Linear Regression and Logistic Regression

[toc]

## Linear Regression

- 最基础的线性回归

<img src="./assets/截屏2025-03-24 18.38.41.png" alt="截屏2025-03-24 18.38.41" style="zoom:50%;" />

- 添加了Linear Basis Function $\phi(x)$

![截屏2025-03-24 18.39.22](./assets/截屏2025-03-24 18.39.22.png)

- Examples of Basis Functions

<img src="./assets/截屏2025-03-24 18.40.24.png" alt="截屏2025-03-24 18.40.24" style="zoom:50%;" />

### Least Square

- Error计算，其中`t`是标签

<img src="./assets/截屏2025-03-24 18.42.23.png" alt="截屏2025-03-24 18.42.23" style="zoom:50%;" />

> **Least Square 最小二乘法**
>
> 通过最小化误差平方和，我们可以得到回归模型的**最佳参数**

### Maximum Likelihood

- 假设label `t` 和目标变量`y`满足下面的关系，其中$\epsilon$是误差项

<img src="./assets/截屏2025-03-24 23.03.08.png" alt="截屏2025-03-24 23.03.08" style="zoom:50%;" />

- 那么可以计算出下面的条件概率

<img src="./assets/截屏2025-03-24 23.05.33.png" alt="截屏2025-03-24 23.05.33" style="zoom:50%;" />

- 那么likelihood function，即似然函数则可以用下面的公式表示

<img src="./assets/截屏2025-03-24 23.06.18.png" alt="截屏2025-03-24 23.06.18" style="zoom:50%;" />

<img src="./assets/截屏2025-03-24 23.06.41.png" alt="截屏2025-03-24 23.06.41" style="zoom:50%;" />

### Gradient Descent

- 接下来用梯度下降法，计算误差`E`对每一个权重`w_i`的偏导

<img src="./assets/截屏2025-03-24 23.08.06.png" alt="截屏2025-03-24 23.08.06" style="zoom:50%;" />

- 让Gradient成0，我们有

<img src="./assets/截屏2025-03-24 23.40.19.png" alt="截屏2025-03-24 23.40.19" style="zoom:50%;" />

### Regularized Least Squares

> 在没有正则化的情况下，模型会通过调整参数来尽可能地减少训练数据中的误差。然而，如果模型过于复杂，可能会出现**过拟合**（overfitting），即模型过于贴合训练数据，导致它对新数据的预测能力差。
>
> 正则化的作用就是通过在损失函数中加入**惩罚项**来抑制模型的复杂度，从而减少过拟合。这样，模型不仅会关注训练数据的拟合，还会限制模型参数的大小，使得它更加平滑，并能更好地泛化到未见过的数据。

- To **avoid over-fitting**, we consider adding a **regularization term** to an error function, so that the total error function to be minimized takes the form
    - λ is the regularization coeﬀicient
    - `E_D` is the data-dependent error, and `E_W` is the regularization term:

<img src="./assets/截屏2025-03-24 23.23.13.png" alt="截屏2025-03-24 23.23.13" style="zoom:50%;" />

<img src="./assets/截屏2025-03-24 23.24.04.png" alt="截屏2025-03-24 23.24.04" style="zoom:50%;" />

- Gradient Descent

<img src="./assets/截屏2025-03-24 23.40.58.png" alt="截屏2025-03-24 23.40.58" style="zoom:50%;" />

- Setting this gradient to zero gives

<img src="./assets/截屏2025-03-24 23.41.11.png" alt="截屏2025-03-24 23.41.11" style="zoom:50%;" />

- A more general regularizer
    - **large λ**: restrict the model’s freedom for fitting data, leading to **high bias and low variance** 
    - **small λ**: warrant more freedom to fit data, resulting in **low bias and high variance**

<img src="./assets/截屏2025-03-24 23.42.22.png" alt="截屏2025-03-24 23.42.22" style="zoom:50%;" />

- **`q=1`**: **L1-lasso regularizer**.
- **`q=2`: L2-ridge regularizer**
- **ElasticNet** 同时引入了L1和L2正则化

<img src="./assets/截屏2025-03-24 23.57.58.png" alt="截屏2025-03-24 23.57.58" style="zoom:50%;" />

### The Bias-Variance Decomposition

<img src="./assets/截屏2025-03-25 00.01.15.png" alt="截屏2025-03-25 00.01.15" style="zoom:50%;" />

> **偏差**（Bias）：模型预测值与真实值之间的差异，表示模型的系统性误差。
>
> **方差**（Variance）：模型预测值的波动性，表示模型对训练数据的敏感程度。
>
> **噪声**（Noise）：数据本身的随机误差，通常是无法控制的，来源于外部因素或测量误差

## Logistic Regression

### Binary Classification

- 对于二元分类，假设有两个类`{C1,C2}`

<img src="./assets/截屏2025-03-25 00.04.41.png" alt="截屏2025-03-25 00.04.41" style="zoom:50%;" />

- 用linear basis function去尝试拟合`a`，即$a = w^T\phi(x)$

<img src="./assets/截屏2025-03-25 00.08.28.png" alt="截屏2025-03-25 00.08.28" style="zoom:50%;" />

- 对于feature `X` 和label `t`，如下

![截屏2025-03-25 00.26.07](./assets/截屏2025-03-25 00.26.07.png)

- Cross-entropy error function

<img src="./assets/截屏2025-03-25 00.26.52.png" alt="截屏2025-03-25 00.26.52" style="zoom:50%;" />

