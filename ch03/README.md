# 第3章：注意力机制实现

## 章节目标

本章将深入理解并实现 Transformer 的核心组件：自注意力机制（Self-Attention）。

## 核心概念

1. **自注意力机制 (Self-Attention)**
   - 理解 Query、Key、Value 的概念
   - 计算注意力权重
   - 实现缩放点积注意力

2. **多头注意力 (Multi-Head Attention)**
   - 并行处理多个注意力头
   - 理解多头注意力的优势
   - 实现完整的多头注意力层

3. **因果注意力 (Causal Attention)**
   - 实现掩码机制
   - 确保模型只能看到过去的 token

## 实现计划

### main/ 目录

核心代码实现：
- [ ] 1. 单个注意力头的实现
- [ ] 2. 多头注意力实现
- [ ] 3. 因果掩码和注意力

### experiments/ 目录

实验和练习：
- [ ] 可视化注意力权重
- [ ] 实验不同的注意力头数量
- [ ] 比较不同的注意力实现方式

## 练习

原书练习题位置：`./ch03/01_main-chapter-code/exercise-solutions.ipynb`

## 学习笔记

### 关键知识点

- **为什么需要注意力机制？**
  - 允许模型关注输入序列的不同部分
  - 捕捉长距离依赖关系

- **Query、Key、Value 的直觉理解**
  - Query: 我在找什么？
  - Key: 我有什么？
  - Value: 实际的内容

### 遇到的问题

_在这里记录遇到的问题和解决方案..._

## 参考资源

- 原书代码: https://github.com/rasbt/LLMs-from-scratch/tree/main/ch03
- "Attention Is All You Need" 论文: https://arxiv.org/abs/1706.03762

---

**状态**: 🔜 待开始
