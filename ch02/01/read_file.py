"""
步骤 2: 读取 the-verdict.txt 文件
功能: 读取文件内容并返回文本字符串
"""

import os


def read_file():
    """读取 the-verdict.txt 文件内容"""

    # 获取当前脚本所在目录
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(curr_dir, "the-verdict.txt")

    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"文件不存在: {file_path}\n"
            f"请先运行 01_generate_file.py 生成文件"
        )

    print(f"正在读取文件: {file_path}")

    # 读取文件内容
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    print(f"✓ 文件读取成功！")
    print(f"  文件大小: {len(raw_text)} 字符")
    print(f"  内容预览 (前 200 字符):\n{raw_text[:200]}")

    return raw_text


if __name__ == "__main__":
    print("=" * 60)
    print("步骤 2: 读取文件")
    print("=" * 60)

    raw_text = read_file()

    print("\n" + "=" * 60)
    print("步骤 2 完成！")
    print("=" * 60)
