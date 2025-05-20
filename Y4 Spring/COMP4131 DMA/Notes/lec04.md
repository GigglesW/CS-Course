# lec04: Analysis and Modeling

[toc]

## Introduction to Analysis and Modeling

**Definitions**

- **Data Analysis**: The process of examining, cleaning, transforming, and interpreting data to extract useful insights and support decision-making.
- **Data Modelling**: The creation of abstract representations (models) to describe, analyze, and predict real-world phenomena.
- **Relationship Between Analysis and Modelling:**
    - Data analysis provides the foundation for modelling by identifying patterns, trends, and relationships in the data.
    - Modelling uses these insights to create predictive or descriptive models.

**The SPAIN Characteristics**

- Specific
- Plausible
- Answerable
- Interesting to a Specific Audience
- Novel

## Data

- **Steven's four level scale**
    - Nominal: **One-hot Encoding**
    - Ordinal: **Label Encoding**
    - Interval
    - Ratio

<img src="./assets/截屏2025-03-10 13.28.47.png" alt="截屏2025-03-10 13.28.47" style="zoom:50%;" />

### Transumeration

- **Def:** 
    - We use **numbers and drawings** to get a sense of a large dataset. 
    - The process is called **Transnumeration**.
- **Four aspects**
    - **Location**: What’s the most common value? 
    - **Variability/Dispersion**: How spread out is the data? What’s a deviant value? 
    - **Shape**: How is the data distributed?
    - **Relationship**: How are two variables linked?
- **Central Tendency**
    - **Mode**: most frequent attribute in the sample
    - **Median**
    - **Arithmetic Mean**
- **Variability**
    - **Range**: min to max, 
    - **Inter-Quartile Range (IQR)**:
- **Shape**
    - **Skewness 偏度**: 它描述了分布形状相对于正态分布的偏斜程度，反映数据是否在均值附近对称分布
    - **Kurtosis 峰度**: Measures how peaked a distribution is.

<img src="./assets/截屏2025-03-10 13.36.00.png" alt="截屏2025-03-10 13.36.00" style="zoom:50%;" />

<img src="./assets/截屏2025-03-10 13.37.01.png" alt="截屏2025-03-10 13.37.01" style="zoom:50%;" />

- **Relationships**
    - **Pearson Correlation Coefficient**: Measures the strength and direction of the linear relationship between two variables.

<img src="./assets/截屏2025-04-26 01.25.40.png" alt="截屏2025-04-26 01.25.40" style="zoom:50%;" />

### Diagnosing Data Problems

- **Check for Boundary Violations:**
    - **Impossible Values:** If a field contains ”Age,” negative values are impossible.
    - **Outliers:** Example: An ”Age” value of 185.
- **Check the Packaging:**
    - Look at the first few rows and the last few rows. Does it all look as expected?
    - Check the dimensions of your dataset (number of observations, number of columns). Does it all match up?
- **Imputation: 填充缺失值**
    - **Unit Imputation**: Impute a data point (e.g., remove a person with missing Age). 
    - **Item Imputation**: Impute a value of a data point (e.g., replace missing Age value).
    - **Hot Deck Imputation**: Replace value by value of previous observation.
    - **Cold Deck Imputation**: Replace value by value randomly sampled from an external dataset. 
    - **Mean Substitution**: Replace value by central value of all other cases (mean/mode/median). 
    - **Regression Imputation**: Use a basic machine learning model to predict the missing value. 
    - **Multiple Imputations**: Sometimes you need more than one method! A lot of design choices go into imputation.

## Data Analysis

**Overview of Data Analysis Techniques**

- Types of Data Analysis
    - Descriptive Analysis 
    - Diagnostic Analysis 
    - Predictive Analysis 
    - Prescriptive Analysis 
    - Exploratory Data Analysis (EDA)

<img src="./assets/截屏2025-03-10 13.42.15.png" alt="截屏2025-03-10 13.42.15" style="zoom:50%;" />

**Descriptive Analysis**

- **Definition**: Summarizes historical data to understand what has happened. 
- **Examples**:
    - Mean, median, mode.
    - Sales reports, customer demographics.

<img src="./assets/截屏2025-03-10 13.43.30.png" alt="截屏2025-03-10 13.43.30" style="zoom:50%;" />

**Diagnostic Analysis**

- **Definition**: Identifies the causes of past events or behaviors. 
- **Examples:**
    - Root cause analysis.
    - Correlation analysis.

<img src="./assets/截屏2025-03-10 13.44.09.png" alt="截屏2025-03-10 13.44.09" style="zoom:50%;" />

**Predictive Analysis**

- **Definition:** Uses historical data to predict future outcomes. 
- **Examples**: Sales forecasting, customer churn prediction.

<img src="./assets/截屏2025-03-10 13.44.40.png" alt="截屏2025-03-10 13.44.40" style="zoom:50%;" />

**Prescriptive Analysis**

- **Definition:** Recommends actions based on data insights. 
- **Examples**: Optimization models, decision trees.

<img src="./assets/截屏2025-03-10 13.45.20.png" alt="截屏2025-03-10 13.45.20" style="zoom:50%;" />

**Exploratory Data Analysis (EDA)**

- **Definition:** Investigates data to discover patterns, trends, and anomalies. 
- **Examples**: Pairplots, heatmaps, summary statistics.

<img src="./assets/截屏2025-03-10 13.45.54.png" alt="截屏2025-03-10 13.45.54" style="zoom:50%;" />

## Data Modeling

**What is a Model**

- **Definition**: A simplified representation of a real-world system.
- **Purpose:** To understand, predict, or simulate real-world phenomena.

**Types of Models**

- **Statistical Models**: 
    - Uses probability and statistical techniques to make inferences from data.
    - Examples: Regression models, time-series models.
- **Machine Learning Models**: 
    - Uses data-driven algorithms to learn patterns and make predictions.
    - Examples: Decision Trees, Neural Networks.
- **Simulation Models**: 
    - Mimics real-world processes using computational techniques.
    - Examples: Monte Carlo simulations, agent-based models.

## Model Evaluation and Validation

- **Train-Test Split**
    - A simple validation technique where data is split into training, validation, and testing sets.
- **Cross-Validation**
    - A more robust method where the dataset is divided into multiple folds.
    - k-Fold Cross-Validation: Data is split into k subsets, and each subset is used for testing once.

### Model Evaluation Metrics

- **Key Metrics for Regression**

    - R 2 (Coeﬀicient of Determination) 

    - RMSE (Root Mean Squared Error) 

    - MAE (Mean Absolute Error)

- **Key Metrics for Classification**

    - Accuracy Precision Recall F1-Score 
    - Confusion Matrix 
    - Receiver Operating Characteristic (ROC) Curve 
    - Area Under the Curve (AUC)

### Bias-Variance Tradeoff

> **Bias** 是指模型的预测值与真实值之间的系统性误差，反映模型的**拟合能力**。
>
> - 偏差较高的模型在训练时会对数据的模式捕获不足，表现为**欠拟合**（Underfitting）。
> - 偏差通常来源于模型过于简单，无法充分学习数据的复杂性。
>
> **Variance** 是指模型对训练数据中的随机噪声的敏感程度，反映模型的**稳定性**。
>
> - 方差较高的模型在训练数据上表现良好，但在测试数据上表现较差，表现为**过拟合**（Overfitting）。
> - 方差通常来源于模型过于复杂，导致对训练数据的噪声进行了过度拟合。

- **Bias**: Error due to overly simplistic assumptions.
- **Variance**: Error due to excessive sensitivity to training data.
    - High bias leads to underfitting.
    - High variance leads to overfitting.
    - The goal is to find an optimal balance between bias and variance.

<img src="./assets/截屏2025-03-10 13.51.23.png" alt="截屏2025-03-10 13.51.23" style="zoom:50%;" />