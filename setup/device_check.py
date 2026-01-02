"""
设备检测和设置工具
用于在 MacBook Pro 上自动检测并设置最佳的计算设备（MPS 或 CPU）
"""

import torch


def get_device():
    """
    获取最佳可用设备

    返回:
        torch.device: MPS 设备（如果可用）或 CPU 设备

    说明:
        - MPS (Metal Performance Shaders): Apple Silicon 的 GPU 加速技术
        - 在 M1/M2/M3 芯片上，MPS 可显著提升训练和推理速度
        - 如果 MPS 不可用，自动回退到 CPU
    """
    if torch.backends.mps.is_available():
        if torch.backends.mps.is_built():
            device = torch.device("mps")
            print("✅ 使用 MPS 加速 (Apple Silicon GPU)")
        else:
            device = torch.device("cpu")
            print("⚠️  MPS 可用但未编译，使用 CPU")
    else:
        device = torch.device("cpu")
        print("⚠️  MPS 不可用，使用 CPU")

    print(f"当前设备: {device}")
    return device


def print_device_info():
    """打印详细的设备信息"""
    print("=" * 60)
    print("🖥️  系统信息")
    print("=" * 60)
    print(f"PyTorch 版本: {torch.__version__}")
    print(f"MPS 可用: {torch.backends.mps.is_available()}")
    print(f"MPS 已构建: {torch.backends.mps.is_built()}")

    # 获取当前设备
    device = get_device()

    # 测试张量创建
    print("\n" + "=" * 60)
    print("🧪 设备测试")
    print("=" * 60)

    # 创建测试张量
    x = torch.randn(1000, 1000).to(device)
    y = torch.randn(1000, 1000).to(device)

    # 执行矩阵乘法
    print(f"执行矩阵乘法 (1000x1000) ...")
    import time
    start = time.time()
    z = torch.matmul(x, y)
    torch.mps.synchronize() if device.type == "mps" else None
    elapsed = time.time() - start

    print(f"✅ 完成! 耗时: {elapsed:.4f} 秒")
    print(f"结果张量形状: {z.shape}, 设备: {z.device}")


def set_tensor_to_device(tensor, device=None):
    """
    将张量移动到指定设备

    参数:
        tensor: PyTorch 张量
        device: 目标设备（如果为 None，使用自动检测的设备）

    返回:
        移动到目标设备的张量
    """
    if device is None:
        device = get_device()
    return tensor.to(device)


def set_model_to_device(model, device=None):
    """
    将模型移动到指定设备

    参数:
        model: PyTorch 模型
        device: 目标设备（如果为 None，使用自动检测的设备）

    返回:
        移动到目标设备的模型
    """
    if device is None:
        device = get_device()

    model = model.to(device)
    print(f"✅ 模型已移动到: {device}")
    return model


if __name__ == "__main__":
    # 打印设备信息
    print_device_info()

    # 示例：创建模型并移动到 MPS
    print("\n" + "=" * 60)
    print("📦 模型设备示例")
    print("=" * 60)

    # 创建一个简单的神经网络
    import torch.nn as nn

    simple_model = nn.Sequential(
        nn.Linear(10, 20),
        nn.ReLU(),
        nn.Linear(20, 10)
    )

    # 将模型移动到最佳设备
    device = get_device()
    simple_model = set_model_to_device(simple_model, device)

    # 测试前向传播
    x = torch.randn(5, 10).to(device)
    output = simple_model(x)
    print(f"✅ 输入形状: {x.shape}, 输出形状: {output.shape}")
