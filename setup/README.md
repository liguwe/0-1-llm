# 环境设置指南（MacBook Pro）

本目录包含环境设置相关的说明和脚本。

## 系统要求

### 硬件要求
- **芯片**: Apple Silicon (M1/M2/M3 系列)
- **内存**: 至少 16GB（推荐 32GB 或更多）
- **存储**: 至少 10GB 可用空间

### 软件要求
- **操作系统**: macOS 12.0+ (Monterey 或更高版本)
- **Python 版本**: 3.10 或 3.11（推荐）
- **Xcode**: 最新版本（用于 MPS 支持）

## Python 版本要求

- **推荐**: Python 3.10 或 3.11
- **最低**: Python 3.9

## 安装步骤

### 1. 创建虚拟环境

```bash
# 使用 venv
python3 -m venv .venv
source .venv/bin/activate

# 或使用 conda
conda create -n llm-from-scratch python=3.11
conda activate llm-from-scratch
```

### 2. 升级 pip

```bash
pip install --upgrade pip
```

### 3. 安装 PyTorch（支持 Apple Silicon MPS 加速）

```bash
# macOS (Apple Silicon) - MPS 加速版本
pip install torch

# 验证安装
python3 -c "import torch; print(f'PyTorch version: {torch.__version__}')"
```

> **注意**: 对于 MacBook Pro (Apple Silicon)，PyTorch 会自动启用 MPS (Metal Performance Shaders) 加速。

### 4. 安装其他依赖

```bash
pip install -r ../requirements.txt
```

### 5. 安装 Jupyter Kernel

```bash
python -m ipykernel install --user --name=llm-from-scratch --display-name "Python (LLM from Scratch)"
```

## 设备检测工具

本项目提供了一个设备检测工具 `device_check.py`，用于自动检测和配置最佳的计算设备。

### 使用方法

```bash
# 运行设备检测
python setup/device_check.py
```

这个脚本会：
- 检测 MPS（Apple Silicon GPU）是否可用
- 显示详细的系统信息
- 测试矩阵乘法性能
- 提供设备设置示例代码

### 在代码中使用

```python
from setup.device_check import get_device, set_model_to_device

# 获取最佳设备
device = get_device()  # 自动选择 MPS 或 CPU

# 将模型移动到设备
model = MyModel()
model = set_model_to_device(model, device)
```

## 验证安装

### 基础验证

```bash
# 验证 PyTorch
python -c "import torch; print(f'PyTorch version: {torch.__version__}')"

# 验证 MPS 加速
python -c "import torch; print(f'MPS Available: {torch.backends.mps.is_available()}')"

# 验证 tiktoken
python -c "import tiktoken; print(f'tiktoken version: {tiktoken.__version__}')"
```

### 完整验证

运行设备检测脚本：
```bash
python setup/device_check.py
```

## MacBook Pro 性能优化

### MPS 加速说明

**MPS (Metal Performance Shaders)** 是 Apple 为 Silicon 芯片提供的 GPU 加速技术：

- **训练速度**: 相比 CPU 可提升 3-10 倍
- **推理速度**: 可提升 5-20 倍
- **内存效率**: 统一内存架构，减少数据传输

### 内存管理建议

如果遇到内存不足（OOM）问题：

```python
# 1. 减小批次大小
batch_size = 8  # 从 64 降到 8 或 16

# 2. 减小模型规模
# GPT_CONFIG = {
#     "vocab_size": 50257,
#     "ctx_len": 256,      # 减小上下文长度
#     "emb_dim": 384,      # 减小嵌入维度
#     "n_heads": 6,        # 减少注意力头数
#     "n_layers": 6,       # 减少层数
# }

# 3. 使用梯度累积
accumulation_steps = 4  # 每 4 个批次更新一次
```

### 监控 GPU 使用

```bash
# 查看实时 GPU 使用情况
sudo powermetrics --samplers gpu_power -i 1000

# 或使用 Activity Monitor（活动监视器）
# 查看 "GPU History" 面板
```

## 推荐的 IDE 设置

### VS Code（推荐）

安装扩展：
- Python (Microsoft)
- Jupyter (Microsoft)
- Pylance (Microsoft)

配置 `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "jupyter.jupyterServerType": "local",
    "python.formatting.provider": "black"
}
```

### PyCharm

- Professional 版本内置 Jupyter 支持
- 配置解释器指向 `.venv`

## 常见问题

### Q1: MPS 不可用怎么办？

**现象**: `torch.backends.mps.is_available()` 返回 `False`

**解决方案**:
1. 确认 macOS 版本 >= 12.0
2. 更新 PyTorch 到最新版本
3. 代码会自动回退到 CPU 运行（速度较慢）

### Q2: 训练时内存不足（OOM）

**解决方案**:
1. 减小 `batch_size`
2. 减小模型参数（层数、嵌入维度）
3. 使用梯度累积
4. 清理不必要的张量：
```python
import torch
torch.mps.empty_cache()  # 清理 MPS 缓存
```

### Q3: MPS 比 CPU 还慢？

**可能原因**:
- 批次太小（GPU 并行优势不明显）
- 数据传输开销过大
- 模型太小（CPU 可能更快）

**建议**: 对于小批量实验，使用 CPU 也可以。

### Q4: tiktoken 安装失败

**解决方案**:
```bash
# 方法 1: 升级 pip 后重试
pip install --upgrade pip
pip install tiktoken

# 方法 2: 使用 conda
conda install -c conda-forge tiktoken
```

## 更多信息

参考官方文档：
- [PyTorch MPS 文档](https://pytorch.org/docs/stable/notes/mps.html)
- [Apple Metal 官方文档](https://developer.apple.com/metal/)
- [原项目 Setup 文档](https://github.com/rasbt/LLMs-from-scratch/tree/main/setup)
