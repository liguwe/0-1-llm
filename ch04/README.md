# 第4章：从零实现 GPT 模型

## 章节目标

本章将把前面学到的组件组合起来，实现一个完整的 GPT（Generative Pre-trained Transformer）模型。

## 核心概念

1. **GPT 架构**
   - 理解 GPT 的整体结构
   - Transformer Decoder 层
   - 层归一化 (Layer Normalization)

2. **前馈神经网络**
   - 位置级别的前馈网络
   - GELU 激活函数
   - 残差连接

3. **模型组装**
   - 将所有组件组合成完整模型
   - 理解模型参数和维度
   - 生成文本（前向传播）

## 实现计划

### main/ 目录

核心代码实现：
- [ ] 1. 实现单个 Transformer Block
- [ ] 2. 实现 GPT 模型
- [ ] 3. 文本生成函数

### experiments/ 目录

实验和练习：
- [ ] 分析不同模型规模的影响
- [ ] 实验不同层数和隐藏层维度
- [ ] FLOPs 分析

## 练习

原书练习题位置：`./ch04/01_main-chapter-code/exercise-solutions.ipynb`

## 学习笔记

### 关键知识点

- **GPT vs BERT**
  - GPT: Decoder-only，自回归生成
  - BERT: Encoder-only，双向理解

- **GPT 模型的关键组件**
  1. Token 嵌入 + 位置编码
  2. 多层 Transformer Block
  3. 最终的线性层输出

### 遇到的问题

_在这里记录遇到的问题和解决方案..._

## 参考资源

- 原书代码: https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04
- GPT 论文: "Language Models are Unsupervised Multitask Learners"

---

**状态**: 🔜 待开始
