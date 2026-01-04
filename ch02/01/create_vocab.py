"""
步骤 4: 创建词汇表 (Vocabulary)
功能: 从 tokens 创建词汇表映射
"""

from typing import List, Dict


def create_vocab(tokens: List[str]) -> Dict[str, int]:
    """
    从 tokens 创建词汇表

    参数:
        tokens: 分词后的列表

    返回:
        vocab: {token: id} 字典
    """

    print("正在创建词汇表...")

    # 1. 去重：使用 set 去掉重复单词
    # 2. 排序：使用 sorted 按字母顺序排列
    all_words = sorted(list(set(tokens)))

    # 3. 查看词汇表大小
    vocab_size = len(all_words)
    print(f"✓ 词汇表创建成功！")
    print(f"  词汇表大小: {vocab_size} 个唯一 tokens")

    # 4. 创建字典：{单词: 整数ID}
    vocab = {token: integer for integer, token in enumerate(all_words)}

    # 打印前 15 个词汇表条目
    print(f"\n  词汇表前 15 个条目:")
    for i, (token, idx) in enumerate(list(vocab.items())[:15]):
        print(f"    {idx:4d}: {repr(token)}")

    # 打印后 5 个词汇表条目
    print(f"\n  词汇表后 5 个条目:")
    for i, (token, idx) in enumerate(list(vocab.items())[-5:]):
        print(f"    {idx:4d}: {repr(token)}")

    return vocab


if __name__ == "__main__":
    print("=" * 60)
    print("步骤 4: 创建词汇表")
    print("=" * 60)

    # 导入步骤 2 和 3 的函数
    from read_file import read_file
    from tokenization import tokenize

    # 读取文件
    raw_text = read_file()
    print()

    # 进行分词
    tokens = tokenize(raw_text)
    print()

    # 创建词汇表
    vocab = create_vocab(tokens)

    print("\n" + "=" * 60)
    print("步骤 4 完成！")
    print("=" * 60)
