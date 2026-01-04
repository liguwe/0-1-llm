"""
步骤 5: 实现分词器类 (Tokenizer Class)
功能: 创建可复用的分词器类，支持编码和解码
"""

import re
from typing import List, Dict


class SimpleTokenizerV1:
    """
    简单分词器 V1 版本
    - 基于预定义的词汇表（vocab）进行编码和解码
    - 使用正则表达式进行文本预处理和分词
    """

    def __init__(self, vocab: Dict[str, int]):
        """
        初始化分词器

        参数:
            vocab (dict): 词汇表字典，格式为 {token_string: token_id}
                         例如: {"hello": 0, "world": 1, ",": 2}

        属性:
            self.str_to_int: 字符串到整数的映射（编码用）
            self.int_to_str: 整数到字符串的映射（解码用）
        """
        # 保存原始词汇表：字符串 -> 整数 ID
        self.str_to_int = vocab

        # 创建反向映射：整数 ID -> 字符串
        # 使用字典推导式，将 vocab 的键值对反转
        # 例如: {"hello": 0, "world": 1} -> {0: "hello", 1: "world"}
        self.int_to_str = {i: s for s, i in vocab.items()}

        print(f"✓ 分词器初始化完成")
        print(f"  词汇表大小: {len(vocab)}")

    def encode(self, text: str) -> List[int]:
        """
        编码方法：将文本转换为整数 ID 序列

        参数:
            text (str): 待编码的文本字符串

        返回:
            list[int]: 整数 ID 列表

        处理流程:
            1. 使用正则表达式分割文本
            2. 去除空白项
            3. 将每个 token 映射为对应的整数 ID
        """
        # 使用正则表达式分割文本
        # 模式说明:
        # - r'(...)': 原始字符串 + 捕获组，保留分隔符
        # - [,.:;?_!"()\']:  匹配常见标点符号
        # - |--:            匹配双连字符
        # - |\s:            匹配任意空白字符（空格、制表符、换行符等）
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        # 清理分词结果：
        # - item.strip(): 去除每个 token 两端的空白字符
        # - if item.strip(): 过滤掉空字符串（只包含空白的项）
        # 使用列表推导式简洁地完成过滤和清理
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]

        # 将清理后的 token 转换为词汇表中的整数 ID
        # 如果 token 不在词汇表中，这里会报 KeyError (V1 版本暂不处理未知单词)
        ids = [self.str_to_int[token] for token in preprocessed]
        return ids

    def decode(self, ids: List[int]) -> str:
        """
        解码方法：将整数 ID 序列还原为文本

        参数:
            ids (list[int]): 整数 ID 列表

        返回:
            str: 解码后的文本字符串

        处理流程:
            1. 将每个整数 ID 映射回对应的字符串 token
            2. 用空格连接所有 token
            3. 使用正则表达式去除标点符号前的多余空格
        """
        # 将整数 ID 列表转换为字符串列表，然后用空格连接
        # 例如: [0, 1, 2] -> ["hello", "world", ","] -> "hello world ,"
        # 对比 JavaScript → ["hello", "world", ","].join(" ")
        text = ' '.join([self.int_to_str[i] for i in ids])

        # 去除标点符号前的多余空格
        # 正则表达式说明:
        # - r'\s+([,.:;?_!"()\'])': 匹配"一个或多个空白字符 + 标点符号"
        # - r'\1': 替换为第一个捕获组（即标点符号本身），去掉前面的空格
        # 例如: "hello , world !" -> "hello, world!"
        # 对比 JavaScript → text.replace(/\s+([,.:;?_!"()\'])/g, "$1");
        text = re.sub(r'\s+([,.:;?_!"()\'])', r'\1', text)
        return text


def test_tokenizer(tokenizer: SimpleTokenizerV1) -> None:
    """
    测试分词器功能

    参数:
        tokenizer: 分词器实例
    """
    print("\n" + "=" * 60)
    print("测试分词器")
    print("=" * 60)

    # 测试文本
    test_text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""

    print(f"测试文本: {test_text}\n")

    # 编码
    ids = tokenizer.encode(test_text)
    print(f"✓ 编码完成")
    print(f"  Token IDs: {ids}")
    print(f"  IDs 数量: {len(ids)}")

    # 解码
    decoded_text = tokenizer.decode(ids)
    print(f"\n✓ 解码完成")
    print(f"  解码文本: {decoded_text}")

    # 验证
    print(f"\n✓ 验证结果:")
    print(f"  原文长度: {len(test_text)}")
    print(f"  解码长度: {len(decoded_text)}")
    print(f"  完全一致: {test_text == decoded_text}")

    # 展示一些 token 映射
    print(f"\n✓ Token 映射示例:")
    for i, token_id in enumerate(ids[:10]):
        token = tokenizer.int_to_str[token_id]
        print(f"    {token_id:4d} -> {repr(token)}")


if __name__ == "__main__":
    print("=" * 60)
    print("步骤 5: 实现分词器类")
    print("=" * 60)

    # 导入前面步骤的函数
    from read_file import read_file
    from tokenization import tokenize
    from create_vocab import create_vocab

    # 读取文件
    print("\n[1/4] 读取文件...")
    raw_text = read_file()

    # 进行分词
    print("\n[2/4] 分词...")
    tokens = tokenize(raw_text)

    # 创建词汇表
    print("\n[3/4] 创建词汇表...")
    vocab = create_vocab(tokens)

    # 创建分词器
    print("\n[4/4] 创建分词器...")
    tokenizer = SimpleTokenizerV1(vocab)

    # 测试分词器
    test_tokenizer(tokenizer)

    print("\n" + "=" * 60)
    print("步骤 5 完成！")
    print("=" * 60)
