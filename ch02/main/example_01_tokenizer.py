"""
第2章示例：文本分词（Tokenization）

这个示例展示如何将文本转换为模型可以理解的数字序列。
分词是 LLM 处理文本的第一步。

核心概念：
    - Token：文本的最小单位，可以是词、子词或字符
    - Tokenizer：将文本转换为 token 序列的工具
    - Token ID：每个 token 对应的唯一数字标识

依赖：
    - tiktoken: OpenAI 的分词器，使用 BPE 算法
"""

import tiktoken


def text_to_token_ids(text: str, tokenizer: tiktoken.Encoding) -> list[int]:
    """
    将文本转换为 token ID 序列

    这是 LLM 理解文本的第一步。分词器将文本切分成小的单位（tokens），
    然后将每个 token 映射为一个唯一的整数 ID。

    参数:
        text: 输入文本，例如 "Hello, world!"
        tokenizer: 分词器实例（tiktoken.Encoding 对象）

    返回:
        token ID 列表，例如 [15496, 11, 1917, 0]

    示例:
        >>> tokenizer = tiktoken.get_encoding("gpt2")
        >>> text_to_token_ids("Hello, world!", tokenizer)
        [15496, 11, 1917, 0]

    注意:
        - 不同的分词器会产生不同的 token 序列
        - GPT-2 使用的是字节对编码（BPE）分词器
        - 标点符号会被单独切分
    """
    # 将文本编码为 token ID
    # tiktoken 的 encode 方法返回一个整数列表
    token_ids = tokenizer.encode(text)

    return token_ids


def token_ids_to_text(token_ids: list[int], tokenizer: tiktoken.Encoding) -> str:
    """
    将 token ID 序列还原为文本

    这是分词的逆过程，用于将模型的输出（token ID）转换为可读的文本。

    参数:
        token_ids: token ID 列表，例如 [15496, 11, 1917, 0]
        tokenizer: 分词器实例

    返回:
        解码后的文本，例如 "Hello, world!"

    示例:
        >>> tokenizer = tiktoken.get_encoding("gpt2")
        >>> token_ids_to_text([15496, 11, 1917, 0], tokenizer)
        'Hello, world!'

    注意:
        - 这个过程应该是完全可逆的
        - 如果 token ID 不在词汇表中，会抛出错误
    """
    # 将 token ID 解码为文本
    text = tokenizer.decode(token_ids)

    return text


def analyze_tokenization(text: str, tokenizer: tiktoken.Encoding) -> None:
    """
    分析文本的分词结果

    展示文本是如何被切分成 tokens 的，帮助理解分词器的工作原理。

    参数:
        text: 要分析的文本
        tokenizer: 分词器实例

    说明:
        这个函数打印出详细的分词信息，包括：
        - 原始文本
        - token ID 序列
        - 每个 token 对应的文本片段
    """
    print("=" * 60)
    print("分词分析")
    print("=" * 60)

    # 打印原始文本
    print(f"原始文本: {text}")
    print()

    # 获取 token IDs
    token_ids = tokenizer.encode(text)
    print(f"Token IDs: {token_ids}")
    print()

    # 逐个解码，展示每个 token 对应的文本
    print("逐个 Token 分析:")
    for i, token_id in enumerate(token_ids):
        # 单独解码这个 token
        token_text = tokenizer.decode([token_id])
        print(f"  Token {i}: ID={token_id:5d}, Text='{token_text}'")

    # 验证完整性
    decoded_text = tokenizer.decode(token_ids)
    print()
    print(f"解码文本: {decoded_text}")
    print(f"是否匹配: {'✅' if decoded_text == text else '❌'}")


def main():
    """
    主函数：演示分词器的使用
    """
    print("第2章示例：文本分词")
    print()

    # 使用 GPT-2 的分词器
    # 这是最常用的分词器之一，也是本书后续章节会使用的
    tokenizer = tiktoken.get_encoding("gpt2")

    # 示例 1: 简单英文句子
    text1 = "Hello, world!"
    analyze_tokenization(text1, tokenizer)
    print()

    # 示例 2: 中文和英文混合
    # 注意：GPT-2 的分词器对中文支持不好，会按字节切分
    text2 = "Learning LLM is fun! 学习 LLM 很有趣！"
    analyze_tokenization(text2, tokenizer)
    print()

    # 示例 3: 长文本
    text3 = """
    Artificial intelligence is transforming the world.
    Large language models like GPT can understand and generate human-like text.
    """
    # 去除首尾空白
    text3 = text3.strip()
    analyze_tokenization(text3, tokenizer)
    print()

    # 统计信息
    print("=" * 60)
    print("分词统计")
    print("=" * 60)

    sample_text = "The quick brown fox jumps over the lazy dog."
    token_ids = tokenizer.encode(sample_text)

    print(f"文本: {sample_text}")
    print(f"字符数: {len(sample_text)}")
    print(f"Token 数: {len(token_ids)}")
    print(f"平均每个 Token 的字符数: {len(sample_text) / len(token_ids):.2f}")
    print()
    print("说明:")
    print("  - 英文平均 1 个 Token ≈ 4 个字符")
    print("  - 中文平均 1 个 Token ≈ 2-3 个汉字（取决于分词器）")
    print("  - GPT-2 的上下文长度是 1024 个 tokens")


if __name__ == "__main__":
    main()
