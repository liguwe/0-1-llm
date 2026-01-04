"""
步骤 3: 分词 (Tokenization)
功能: 将文本分割成 tokens
"""

import re
from typing import List


def tokenize(raw_text: str) -> List[str]:
    """
    将文本分割成 tokens

    参数:
        raw_text: 原始文本字符串

    返回:
        tokens: 分词后的列表
    """

    print("正在进行分词...")

    # 使用正则表达式进行分词
    # 模式说明：
    # - r'(...)': 原始字符串 + 捕获组，保留分隔符
    # - [,.:;?_!"()\']:  匹配常见标点符号
    # - |--:            匹配双连字符
    # - |\s:            匹配任意空白字符（空格、制表符、换行符等）
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

    # 清理分词结果：
    # - item.strip(): 去除每个 token 两端的空白字符
    # - if item.strip(): 过滤掉空字符串（只包含空白的项）
    tokens = [item.strip() for item in preprocessed if item.strip()]

    print(f"✓ 分词完成！")
    print(f"  总 token 数: {len(tokens)}")
    print(f"  前 50 个 tokens:")

    # 打印前 50 个 tokens，每行 10 个
    for i in range(0, min(50, len(tokens)), 10):
        batch = tokens[i:i+10]
        print(f"    [{i:3d}-{i+len(batch)-1:3d}] {batch}")

    return tokens


if __name__ == "__main__":
    print("=" * 60)
    print("步骤 3: 分词")
    print("=" * 60)

    # 导入步骤 2 的函数
    from read_file import read_file

    # 读取文件
    raw_text = read_file()
    print()

    # 进行分词
    tokens = tokenize(raw_text)

    print("\n" + "=" * 60)
    print("步骤 3 完成！")
    print("=" * 60)
