import tiktoken


def test_unknown_words(test_text):
    """
    测试未知词汇（Out-of-vocabulary words）的分词效果
    
    参数:
        test_text (str): 包含未知词汇的测试文本
    """
    tokenizer = tiktoken.get_encoding("gpt2")

    print(f"\n原始文本: {repr(test_text)}")
    print("=" * 60)
    
    # 编码
    ids = tokenizer.encode(test_text)
    print(f'Token IDs: {ids}')
    print(f'Token 数量: {len(ids)}\n')

    # 打印每个 token 的详细映射
    print("Token ID 和文本的映射关系:")
    print("─" * 60)
    for i, token_id in enumerate(ids):
        # 解码单个 token ID 得到对应的文本
        token_text = tokenizer.decode_single_token_bytes(token_id).decode('utf-8', errors='replace')
        print(f"  第 {i+1:2d} 个: ID={token_id:5d} -> {repr(token_text)}")
    print()

    # 解码
    decoded_text = tokenizer.decode(ids)
    print(f"解码后的文本: {repr(decoded_text)}")


test_text = "Akwirw ier"

test_unknown_words(test_text)
