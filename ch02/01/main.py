"""
步骤 6: 主程序 (Main)
功能: 执行完整的分词器流程（步骤 1-5）
"""

import os
import sys


def print_separator(title: str = "") -> None:
    """打印分隔线"""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")
        print("=" * 70)


def main():
    """执行完整的分词器构建流程"""

    print("\n" + "🚀" * 35)
    print(" " * 15 + "LLM 分词器完整流程")
    print(" " * 10 + "执行步骤 1-6：从文件生成到分词器测试")
    print("🚀" * 35)

    # ========== 步骤 1: 生成文件 ==========
    print_separator("步骤 1: 生成/下载文件")
    from generate_file import generate_file
    file_path = generate_file()
    print(f"✓ 步骤 1 完成: 文件已准备好")

    # ========== 步骤 2: 读取文件 ==========
    print_separator("步骤 2: 读取文件内容")
    from read_file import read_file
    raw_text = read_file()
    print(f"✓ 步骤 2 完成: 文本已读取 ({len(raw_text)} 字符)")

    # ========== 步骤 3: 分词 ==========
    print_separator("步骤 3: 分词处理")
    from tokenization import tokenize
    tokens = tokenize(raw_text)
    print(f"✓ 步骤 3 完成: 获得 {len(tokens)} 个 tokens")

    # ========== 步骤 4: 创建词汇表 ==========
    print_separator("步骤 4: 创建词汇表")
    from create_vocab import create_vocab
    vocab = create_vocab(tokens)
    print(f"✓ 步骤 4 完成: 词汇表包含 {len(vocab)} 个唯一 tokens")

    # ========== 步骤 5: 实现分词器类 ==========
    print_separator("步骤 5: 初始化分词器")
    from tokenizer_class import SimpleTokenizerV1
    tokenizer = SimpleTokenizerV1(vocab)
    print(f"✓ 步骤 5 完成: 分词器已创建")

    # ========== 步骤 6: 测试分词器 ==========
    print_separator("步骤 6: 测试分词器")

    # 测试 1: 基本编码解码
    print("\n[测试 1] 基本编码解码")
    print("-" * 70)

    test_text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
    print(f"原文: {test_text}")

    # 编码
    ids = tokenizer.encode(test_text)
    print(f"\n编码结果:")
    print(f"  Token 数量: {len(ids)}")
    print(f"  Token IDs: {ids[:10]}... (显示前 10 个)")

    # 解码
    decoded_text = tokenizer.decode(ids)
    print(f"\n解码结果:")
    print(f"  文本: {decoded_text}")
    print(f"  一致性: {'✓ 通过' if test_text == decoded_text else '✗ 失败'}")

    # 测试 2: 使用训练文本中的句子
    print("\n[测试 2] 训练文本句子处理")
    print("-" * 70)

    # 从原始文本中提取一个句子进行测试
    test_text2 = "I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough."
    print(f"原文: {test_text2}")

    try:
        ids2 = tokenizer.encode(test_text2)
        decoded2 = tokenizer.decode(ids2)

        print(f"\nToken 数量: {len(ids2)}")
        print(f"解码文本: {decoded2}")
        print(f"一致性: {'✓ 通过' if test_text2 == decoded2 else '✗ 失败'}")
    except KeyError as e:
        print(f"\n✗ 测试失败: 词汇表中不存在词 {e}")
        print("  (V1 版分词器不支持未知词)")

    # 测试 3: 展示词汇表统计
    print("\n[测试 3] 词汇表统计")
    print("-" * 70)

    # 统计信息
    total_tokens = len(tokens)
    unique_tokens = len(vocab)
    avg_token_length = sum(len(t) for t in tokens) / len(tokens)

    print(f"  总 token 数: {total_tokens}")
    print(f"  唯一 token 数: {unique_tokens}")
    print(f"  平均 token 长度: {avg_token_length:.2f} 字符")

    # 展示一些特殊的 tokens
    print(f"\n  特殊 tokens 示例:")
    special_tokens = ['"', '--', '(', ')', ',', '.', '!', '?']
    for token in special_tokens:
        if token in vocab:
            print(f"    {repr(token):>6} -> ID: {vocab[token]:4d}")

    # ========== 完成 ==========
    print_separator("✨ 所有步骤完成！")
    print("\n分词器已成功构建并测试！")
    print("\n📊 总结:")
    print(f"  • 文件: {os.path.basename(file_path)}")
    print(f"  • 文本大小: {len(raw_text)} 字符")
    print(f"  • Token 总数: {len(tokens)}")
    print(f"  • 词汇表大小: {len(vocab)}")
    print(f"  • 分词器: SimpleTokenizerV1")
    print("\n" + "🎉" * 35 + "\n")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"\n❌ 错误: {e}")
        print("\n请确保所有步骤文件都在当前目录中，并且按顺序执行。")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
