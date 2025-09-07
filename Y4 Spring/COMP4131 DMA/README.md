# COMP4131 DMA

>   写于 2025 年 9 月 7 日 

## 1. Basic Info

| Title       | Content                                 | Remark           |
| ----------- | --------------------------------------- | ---------------- |
| Module Code | COMP4131                                | Master's Module  |
| Name        | Data Modeling and Analysis              | **DMA** in short |
| Credits     | 20                                      |                  |
| Lecture     | 1 per week                              | 2h               |
| Lab         | 1 per week                              | 2h               |
| Lab Work    | 10 * 2.5% lab submission                | 25%              |
| CW          | Report: choose a dataset to perform DMA | 75%              |

## 2. Lecture

这门课是**研究生课程**，内容几乎完全 Cover 秋季ML，并且不用考试，很推荐选择，由 [Kian Ming Lim](https://www.nottingham.edu.cn/cn/People/Profile.aspx?id=e5d4ef32-a493-4daf-8b34-babc3487d469&language=zh) 和 [Daokun Zhang](https://www.nottingham.edu.cn/cn/Info-Hub/Staff-Profile.aspx?id=2dd7b178-526f-4477-ac89-e05bc8c5a7da&language=zh) 负责。

此课编排尤为清晰连贯，可能是继承英诺原的缘故，编排质量在宁诺CS里纯纯T0级别。从课程内容上看，与其叫 Data Modeling and Analysis，不如直接叫 Data Science and Machine Learning

- Lec01-04：Data Science部分，讲了数据预处理、可视化和如何建模等等
- Lec05-10：Machine Learning部分，对数据建模部分展开介绍，Classification、Regression和Unsupervised的模型均有涉及

Lecture 的内容讲的很深，特别是第二部分，把很详细的数学推导公式都放上去了，按宁诺大一和MCS里学到的数学工具完全不足以理解。我看明白模型的基本原理后就不管具体的数学了，毕竟代码里也就是调库，知道哪些参数怎么调就行。后来听老师说，因为这门课没有Exam，所以他希望在课上把原理讲清楚点。

## 3. Lab

Lab 是完全照搬英诺，写得非常清晰，难度适中。

- DS部分的强度挺大，跟着做完基本整个Lab就结束了。
- ML部分基本也都是调库 [SciKit-Learn](https://scikit-learn.org/stable/)，知道哪几个参数要调，每个参数是什么影响就行

## 4. CW

这门课的 CW 是我在宁诺写过最“Project”的一个，体验感很好，因为他真正做到了一个项目从头到尾的全流程，并且很好的把整门课教的内容都用上了。

CW 的要求是在网络上自由找一个数据集（对数据集的质量会有些要求），然后用课内涉及到的算法（也可以是更Advanced的）在数据集上跑，对比每个算法的优劣，产出一篇报告，报告格式直接要求[IEEE会议。](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn)

所以这个CW本质上就是个 Project，或者说 Research，要自己找数据集，数据清洗/预处理，可视化，挑出/删掉一些不好的feature，然后用不同的算法对此建模。每个算法又需要用GridSearch找到最优的参数组合，并分析每个参数对该算法在该数据集上的影响，最后找到最好的算法及其参数组合，并分析原因。

总之，虽然我非常喜欢这门课的编排和设置，但是它的**给分确实堪忧**，最后只拿到**65+**。虽然我的report没有很优质，但按照本科其他课的给分要求，应该罪不至此。或许研究生课程的给分会更苛刻，又或许其他人的report都很出彩，确实技不如人。具体原因无从知晓，祝你们好运。
