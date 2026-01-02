# 代码注释规范（中文）

本项目的所有代码都必须使用**中文注释**，以便加深理解和便于日后复习。

## 注释原则

### 1. 为什么要中文注释？

- **深化理解**: 用中文解释概念，强迫自己真正理解而非"翻译"
- **便于复习**: 日后阅读代码时，中文注释更容易理解
- **促进分享**: 方便与他人交流讨论

### 2. 注释的质量标准

#### 好的注释 ✅

```python
# 将输入文本转换为 token ID 序列
# 输入: "Hello world" -> 输出: [15496, 995]
# 这是 GPT 模型理解文本的第一步
def tokenize(text):
    ...
```

#### 不好的注释 ❌

```python
# tokenize function
def tokenize(text):
    ...
```

## 具体规范

### 1. 文件级注释

每个 `.py` 文件开头应有：

```python
"""
模块名称：xxx
用途：实现 xxx 功能
作者：xxx
日期：xxx

核心概念：
    - 概念1的中文解释
    - 概念2的中文解释

依赖：
    - torch: PyTorch 深度学习框架
    - numpy: 数值计算
"""
```

### 2. 函数注释

```python
def function_name(param1, param2):
    """
    函数功能的简要说明（中文）

    详细说明这个函数做什么，为什么这么做，算法的核心思想。

    参数:
        param1 (类型): 参数1的中文说明，包括取值范围和物理意义
        param2 (类型): 参数2的中文说明

    返回:
        返回值类型: 返回值的中文说明

    示例:
        >>> function_name(10, 20)
        返回值解释

    注意:
        - 使用时需要注意的事项
        - 可能的边界情况
    """
    pass
```

### 3. 类注释

```python
class ClassName:
    """
    类名的中文说明

    这个类的作用和设计思路。

    属性:
        attr1: 属性1的中文说明
        attr2: 属性2的中文说明

    方法:
        method1: 方法1的中文说明
        method2: 方法2的中文说明
    """

    def __init__(self, param1, param2):
        """
        初始化对象

        参数:
            param1: 参数说明
            param2: 参数说明
        """
        pass
```

### 4. 关键算法步骤注释

```python
# Step 1: 计算注意力权重
# Q、K、V 分别代表 Query（查询）、Key（键）、Value（值）
# 这是 Transformer 的核心机制，让模型能够关注输入的不同部分
attention_scores = torch.matmul(Q, K.transpose(-2, -1))

# Step 2: 缩放注意力分数
# 除以 sqrt(d_k) 是为了防止点积结果过大导致梯度消失
# d_k 是 key 的维度
attention_scores = attention_scores / math.sqrt(d_k)

# Step 3: 应用 softmax 获得注意力权重
# softmax 将分数转换为概率分布，所有权重和为 1
attention_weights = F.softmax(attention_scores, dim=-1)

# Step 4: 加权求和
# 用注意力权重对 Value 进行加权求和，得到最终输出
output = torch.matmul(attention_weights, V)
```

### 5. 数学公式注释

```python
# 位置编码公式：PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
#                 PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
# 其中:
#   - pos: 位置索引 (0, 1, 2, ...)
#   - i:  维度索引 (0, 1, 2, ...)
#   - d_model: 模型的嵌入维度
#
# 这个公式让模型能够区分不同位置的 token
# 使用 sin 和 cos 让模型能够学习相对位置关系
def positional_encoding(seq_len, d_model):
    ...
```

### 6. 超参数注释

```python
class GPTConfig:
    """
    GPT 模型的超参数配置

    这些超参数的选择基于以下考虑：
    - 增加层数和维度会提升性能，但也增加计算量
    - 对于 MacBook Pro，需要平衡性能和内存占用
    """

    # 词汇表大小：GPT-2 使用 50257 个 token
    # 这个大小涵盖了英文中常见的词和子词
    vocab_size: int = 50257

    # 上下文长度：模型能处理的最大序列长度
    # 256 适合快速实验，GPT-2 使用 1024，GPT-3 使用 2048
    ctx_len: int = 256  # 实验时使用较小值以节省内存

    # 嵌入维度：每个 token 被映射成的向量长度
    # 更大的维度能表示更丰富的语义，但也增加计算量
    # GPT-2 small 使用 768，这里用 384 以适应 MacBook
    emb_dim: int = 384

    # 注意力头数：多头注意力让模型能关注不同的语义层面
    # 必须能整除 emb_dim（384 / 6 = 64，每个头的维度）
    n_heads: int = 6

    # 层数：Transformer Block 的数量
    # 更多的层数让模型能学习更复杂的模式
    # GPT-2 small 使用 12 层，这里用 6 层以加快训练
    n_layers: int = 6

    # Dropout 概率：随机丢弃一部分神经元以防止过拟合
    # 0.1 是常用的默认值
    drop_prob: float = 0.1

    # QKV 偏置：是否在计算 Q、K、V 时使用偏置项
    # 原始 Transformer 论文使用了偏置
    qkv_bias: bool = False
```

### 7. 行内注释

```python
# 创建嵌入层：将 token ID 转换为稠密向量
# 这一步让离散的 token ID 变为连续的向量表示
tok_emb = self.tok_emb(token_ids)  # (batch_size, seq_len, emb_dim)

# 创建位置编码：让模型知道每个 token 的位置
# 位置编码是可学习的参数，随模型训练优化
pos_emb = self.pos_emb(
    torch.arange(seq_len, device=device)
)  # (seq_len, emb_dim)

# 将 token 嵌入和位置编码相加
# 这让模型同时考虑 token 的语义和位置信息
x = tok_emb + pos_emb  # 广播机制
```

## 注释的最佳实践

### 1. 解释"为什么"，而不是"做什么"

```python
# ❌ 不好：只说了做什么
x = x + 5  # 加 5

# ✅ 好：解释了为什么
# 偏移位置索引，从 0-based 改为 1-based
x = x + 5
```

### 2. 对非显而易见的代码添加注释

```python
# PyTorch 的 softmax 默认在最后一个维度上计算
# 但这里我们需要在倒数第二个维度（vocabulary）上计算
# 所以明确指定 dim=-1
logits = self.out_head(x)  # (batch_size, seq_len, vocab_size)
loss = F.cross_entropy(
    logits.reshape(-1, logits.shape[-1]),  # 展平前两维
    targets.reshape(-1),                   # 展平前两维
)
```

### 3. 使用注释标记待办事项

```python
# TODO: 添加层归一化的 epsilon 参数
# FIXME: 这里可能存在数值稳定性问题
# NOTE: 这种实现方式内存效率较低
# HACK: 临时解决方案，需要重构
```

### 4. 对实验性代码添加注释

```python
# 实验：使用 GeLU 替代 ReLU
# GeLU 在 Transformer 中表现更好，但计算稍慢
# 如果训练太慢，可以改回 ReLU
x = F.gelu(x)
```

## 常见术语对照表

在注释中使用中文时，专业术语可以保留英文或中英混用：

| 英文 | 中文 | 说明 |
|------|------|------|
| Token | Token / 词元 | 可直接使用英文 |
| Embedding | 嵌入 / 词嵌入 | 两者都常用 |
| Attention | 注意力 | 可直接使用英文 |
| Transformer | Transformer | 专有名词，保留英文 |
| Forward pass | 前向传播 | 中英混用 |
| Backpropagation | 反向传播 | 中英混用 |
| Gradient | 梯度 | 可直接使用英文 |
| Learning rate | 学习率 | 中英混用 |
| Overfitting | 过拟合 | 可直接使用英文 |
| Fine-tuning | 微调 | 可直接使用英文 |
| Pre-training | 预训练 | 可直接使用英文 |

## 注释模板

### PyTorch 模型模板

```python
class TransformerBlock(nn.Module):
    """
    Transformer 块：GPT 模型的基本构建单元

    这个块包含两个主要子层：
    1. 多头自注意力层
    2. 前馈神经网络层

    每个子层都采用残差连接和层归一化。
    """

    def __init__(self, cfg):
        super().__init__()
        # 多头注意力层
        # 让模型能够关注输入序列的不同部分
        self.att = MultiHeadAttention(cfg)

        # 前馈神经网络
        # 对每个位置独立地进行非线性变换
        self.ff = FeedForward(cfg)

        # 层归一化 1：在注意力之前
        # 有助于稳定训练过程
        self.norm1 = LayerNorm(cfg)

        # 层归一化 2：在前馈网络之前
        self.norm2 = LayerNorm(cfg)

        # Dropout 防止过拟合
        self.drop_resid = nn.Dropout(cfg.drop_prob)

    def forward(self, x):
        """
        前向传播

        参数:
            x (Tensor): 输入张量，形状 (batch_size, seq_len, emb_dim)

        返回:
            Tensor: 输出张量，形状与输入相同

        流程:
            1. 层归一化
            2. 多头注意力
            3. 残差连接
            4. 层归一化
            5. 前馈网络
            6. 残差连接
        """
        # 注意力子层 + 残差连接
        # 先归一化，再计算注意力，最后加上残差
        residual = x  # 保存输入用于残差连接
        x = self.norm1(x)  # 层归一化
        x = self.att(x)  # 多头注意力
        x = self.drop_resid(x)  # Dropout
        x = x + residual  # 残差连接

        # 前馈网络子层 + 残差连接
        residual = x  # 保存输入用于残差连接
        x = self.norm2(x)  # 层归一化
        x = self.ff(x)  # 前馈网络
        x = self.drop_resid(x)  # Dropout
        x = x + residual  # 残差连接

        return x
```

## 检查清单

在提交代码前，确保：

- [ ] 所有函数都有中文文档字符串
- [ ] 所有类都有中文说明
- [ ] 关键算法步骤都有中文注释
- [ ] 数学公式都有中文解释
- [ ] 超参数都有选择原因的说明
- [ ] 没有"自解释"的无意义注释
- [ ] 注释解释了"为什么"，而不是"做什么"

## 参考资料

- [Python 文档字符串规范 (PEP 257)](https://peps.python.org/pep-0257/)
- [Google Python 风格指南](https://google.github.io/styleguide/pyguide.html)

---

**记住：好的注释是给未来的自己和他人看的！**
