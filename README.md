# 0-1 LLM: From Scratch to Mastery

## 项目目标

这是一个从 0 到 1 复刻 [Sebastian Raschka 的《Build a Large Language Model (From Scratch)》(LLMs-from-scratch)](https://github.com/rasbt/LLMs-from-scratch) 的学习项目。

**核心原则：手动敲代码，建立肌肉记忆 + 中文注释，深化理解**

本项目的核心理念是通过**亲手实现每一个组件**来深入理解大语言模型（LLM）的工作原理，而不是简单地复制粘贴代码。每个章节的核心代码都将由我手动编写，以培养真正的理解和编程直觉。

**代码注释原则：所有代码使用中文注释**
- ✅ 所有函数、类、变量都有中文注释说明其用途
- ✅ 关键算法步骤都有详细的中文解释
- ✅ 复杂的数学概念都有中文说明和公式解释
- 🎯 目标：通过中文注释加深理解，方便日后复习和分享

## 学习路径

本项目按照原书章节结构组织，涵盖以下核心内容：

### 章节概览

| 章节 | 内容 | 状态 |
|------|------|------|
| **Ch 1** | 理解大语言模型 | 🔜 待开始 |
| **Ch 2** | 文本数据处理 | 🔜 待开始 |
| **Ch 3** | 注意力机制实现 | 🔜 待开始 |
| **Ch 4** | 从零实现 GPT 模型 | 🔜 待开始 |
| **Ch 5** | 无标签数据预训练 | 🔜 待开始 |
| **Ch 6** | 文本分类微调 | 🔜 待开始 |
| **Ch 7** | 指令遵循微调 | 🔜 待开始 |
| **附录 A** | PyTorch 入门 | 🔜 待开始 |

### 技术栈

- **深度学习框架**: PyTorch（支持 MPS 加速，适配 Apple Silicon）
- **编程语言**: Python 3.10+
- **开发工具**: Jupyter Notebook / VS Code
- **运行平台**: MacBook Pro（Apple Silicon M1/M2/M3 芯片）
- **加速方案**: Metal Performance Shaders (MPS) - Apple 的 GPU 加速技术

## 项目结构

```
0-1-llm/
├── README.md                    # 项目说明文档
├── CODING_STANDARDS.md          # 代码注释规范（重要！）
├── requirements.txt             # Python 依赖
├── setup/                       # 环境设置相关
│   ├── README.md               # MacBook Pro 环境设置指南
│   └── device_check.py         # 设备检测工具（MPS/CPU）
├── ch02/                        # 第2章：文本数据处理
│   ├── main/                    # 核心代码（手动实现）
│   │   └── example_01_tokenizer.py  # 分词器示例
│   ├── experiments/             # 实验和练习
│   └── README.md                # 章节说明
├── ch03/                        # 第3章：注意力机制
│   ├── main/
│   ├── experiments/
│   └── README.md
├── ch04/                        # 第4章：GPT 模型
│   ├── main/
│   ├── experiments/
│   └── README.md
├── ch05/                        # 第5章：预训练
│   ├── main/
│   ├── experiments/
│   └── README.md
├── ch06/                        # 第6章：分类微调
│   ├── main/
│   ├── experiments/
│   └── README.md
├── ch07/                        # 第7章：指令微调
│   ├── main/
│   ├── experiments/
│   └── README.md
└── appendix-A/                  # 附录：PyTorch 入门
    ├── main/
    ├── experiments/
    └── README.md
```

## 学习方法

### 1. 手动实现原则
- ✅ **推荐**: 参考原书和原仓库的思路，自己手敲代码
- ❌ **避免**: 直接复制粘贴大段代码
- 🎯 **目标**: 通过手动编码建立深度理解和肌肉记忆

### 2. 代码注释原则（重要！）
- ✅ **所有代码使用中文注释**
  - 函数和类：说明功能、参数、返回值
  - 关键步骤：解释算法逻辑和原理
  - 数学公式：用中文解释含义和用途
  - 超参数：说明选择原因和影响
- 📝 **注释质量要求**
  - 不仅是"做什么"，更要解释"为什么"
  - 对复杂的 Transformer 组件要有详细的中文说明
  - 便于日后复习和与他人交流

> 📖 **详细的注释规范请参考**: [CODING_STANDARDS.md](./CODING_STANDARDS.md)

### 3. 实验和探索
每个章节包含：
- `main/` 目录：核心概念的实现代码
- `experiments/` 目录：个人实验、练习和扩展
- 可视化和调试代码，帮助理解模型行为

### 4. 进度跟踪
- 每完成一个章节，更新上表中的状态
- 在章节目录的 README.md 中记录学习笔记和心得
- 记录遇到的问题和解决方案

## 环境设置（MacBook Pro）

### 系统要求

- **操作系统**: macOS 12.0+ (Monterey 或更高版本)
- **芯片**: Apple Silicon (M1/M2/M3/M3 Pro/M3 Max)
- **内存**: 至少 16GB（推荐 32GB 或更多）
- **存储**: 至少 10GB 可用空间

### 快速开始

```bash
# 1. 创建虚拟环境（使用 Python 3.10 或 3.11）
python3 -m venv .venv
source .venv/bin/activate

# 2. 升级 pip
pip install --upgrade pip

# 3. 安装 PyTorch（支持 Apple Silicon 的 MPS 加速）
pip install torch

# 4. 安装其他依赖
pip install -r requirements.txt

# 5. 验证 MPS 加速是否可用
python3 -c "import torch; print(f'MPS Available: {torch.backends.mps.is_available()}'); print(f'MPS Built: {torch.backends.mps.is_built()}')"
```

### MacBook Pro 优化说明

#### MPS (Metal Performance Shaders) 加速
- Apple Silicon 芯片的 GPU 加速技术
- 性能接近 CUDA，适合训练中小型模型
- 自动检测并使用 GPU（无需额外配置）

#### 性能建议
- **小型模型训练**: 使用 MPS 加速（推荐）
- **数据预处理**: 可在 CPU 上运行
- **推理和生成**: MPS 加速能显著提升速度
- **内存优化**: 批处理大小不宜过大，避免内存溢出

#### Q1: MPS 不可用怎么办？
如果 MPS 不可用，代码会自动在 CPU 上运行，只是速度较慢：
```python
# 检测并设置设备
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")
```

#### Q2: 训练时内存不足？
- 减小 `batch_size`（如从 64 降到 16 或 8）
- 减小模型参数（如更少的层数或更小的隐藏层维度）
- 使用梯度累积来模拟更大的批次

#### Q3: 如何监控 GPU 使用情况？
```bash
# 查看 GPU 使用率
sudo powermetrics --samplers gpu_power -i 1000
```

### 主要依赖

- `torch` - PyTorch 深度学习框架（支持 Apple Silicon MPS 加速）
- `tiktoken` - OpenAI 的分词器
- `numpy` - 数值计算
- `matplotlib` - 可视化
- `jupyter` - Jupyter Notebook

## 参考资源

### 官方资源
- 📖 [原书主页 (Manning)](https://www.manning.com/books/build-a-large-language-model-from-scratch)
- 💻 [官方代码仓库](https://github.com/rasbt/LLMs-from-scratch)
- 🎥 [配套视频课程](https://www.manning.com/livevideo/build-a-large-language-model-from-scratch-livelessons)
- 📝 [练习题和解答](https://github.com/rasbt/LLMs-from-scratch/tree/main/appendix-C)

### 相关资源
- [Build A Reasoning Model (From Scratch)](https://github.com/rasbt/reasoning-from-scratch) - 作者的另一本书，专注于推理模型

## 学习笔记

### 为什么要从零实现？

1. **深入理解**: 知其然，更知其所以然
2. **调试能力**: 当模型出问题时，能够快速定位问题
3. **创新能力**: 只有理解基础，才能进行有意义的改进
4. **面试准备**: 掌握底层原理，轻松应对技术面试

### 预期收获

完成本项目后，你将能够：
- 🎯 理解 Transformer 架构的每个组件
- 🔧 从零实现一个 GPT 风格的语言模型
- 🏋️ 训练自己的小型语言模型
- 🎨 对预训练模型进行微调以适应特定任务
- 📊 理解并实现现代 LLM 的关键技术

## 进度追踪

- **开始日期**: 2026-01-02
- **当前章节**: Ch 1
- **完成度**: 0%

## 许可证

本项目仅供学习使用。核心内容基于 [ Sebastian Raschka 的《Build a Large Language Model (From Scratch)》](https://github.com/rasbt/LLMs-from-scratch)，请参考原仓库的许可证信息。

---

**Let's build an LLM from scratch! 🚀**
