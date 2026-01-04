import tiktoken

def test_tiktoken(text):
    # 使用gpt2分词器
    tokenizer = tiktoken.get_encoding("gpt2")

    print(f"\n原始文本: {text}")
    print("=" * 60)
    
    # 编码
    ids = tokenizer.encode(text)
    print(f'IDs: {ids}')
    print(f'IDs 数量: {len(ids)}\n')

    # 打印 ID -> Token 的映射关系
    print("Token ID 和文本的映射关系:")
    print("─" * 60)
    for token_id in ids:
        # 解码单个 token ID 得到对应的文本
        token_text = tokenizer.decode_single_token_bytes(token_id).decode('utf-8', errors='replace')
        print(f"  {token_id:5d}: {repr(token_text)}")
    print()

    # 解码
    decoded_text = tokenizer.decode(ids)
    print(f"解码后的文本: {decoded_text}")

test_tiktoken('Hello world, machine_learning someunknownPlace and data-preprocessing tasks!')
