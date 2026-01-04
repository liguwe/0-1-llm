"""
步骤 1: 生成/下载 the-verdict.txt 文件
功能: 从远程 URL 下载文本文件到本地
"""

import os
import requests

def generate_file():
    """下载 the-verdict.txt 文件到本地"""

    # 获取当前脚本所在目录
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(curr_dir, "the-verdict.txt")

    # 如果文件已存在，询问是否重新下载
    if os.path.exists(file_path):
        print(f"✓ 文件已存在: {file_path}")
        return file_path

    # 下载 URL
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

    print(f"正在从远程下载文件...")
    print(f"URL: {url}")
    print(f"保存到: {file_path}")

    try:
        # 发送 GET 请求
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # 检查请求是否成功

        # 写入文件
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✓ 文件下载成功！")
        print(f"  文件大小: {len(response.content)} 字节")

        # 预览前 200 个字符
        with open(file_path, "r", encoding="utf-8") as f:
            preview = f.read(200)
            print(f"  内容预览:\n{preview}")

        return file_path

    except Exception as e:
        print(f"✗ 下载失败: {e}")
        raise


if __name__ == "__main__":
    print("=" * 60)
    print("步骤 1: 生成文件")
    print("=" * 60)

    file_path = generate_file()

    print("\n" + "=" * 60)
    print("步骤 1 完成！")
    print("=" * 60)
