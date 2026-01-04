# 第①步：读取 the-verdict.txt
import os
import re

# 获取当前脚本所在目录
curr_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_dir, "the-verdict.txt")

# 读取文件内容
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

print(f"文件读取成功，总字符数: {len(raw_text)}")
print(f"前 200 个字符预览:\n{raw_text[:200]}")
print("\n" + "="*50 + "\n")

# 第②步：实现分词器，将 text 文件分词成很多 token

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

print(f"分词完成，总 token 数: {len(tokens)}")
print(f"前 50 个 tokens:")
print(tokens[:50])
print("\n" + "="*50 + "\n")

# 第③步：创建词汇表（Vocabulary）

# 1. 去重：使用 set 去掉重复单词
# 2. 排序：使用 sorted 按字母顺序排列
all_words = sorted(list(set(tokens)))

# 3. 查看词汇表大小
vocab_size = len(all_words)
print(f"词汇表大小: {vocab_size}")

# 4. 创建字典：{单词: 整数ID}
vocab = {token: integer for integer, token in enumerate(all_words)}

print(f"\n词汇表前 10 个条目:")
for i, (token, idx) in enumerate(list(vocab.items())[:10]):
    print(f"  {token}: {idx}")
print("\n" + "="*50 + "\n")

# 第④步：实现简单的分词器类

class SimpleTokenizerV1:
    """
    简单分词器 V1 版本
    - 基于预定义的词汇表（vocab）进行编码和解码
    - 使用正则表达式进行文本预处理和分词
    """

    def __init__(self, vocab):
        """
        初始化分词器

        参数:
            vocab (dict): 词汇表字典，格式为 {token_string: token_id}
        """
        # 保存原始词汇表：字符串 -> 整数 ID
        self.str_to_int = vocab

        # 创建反向映射：整数 ID -> 字符串
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        """
        编码方法：将文本转换为整数 ID 序列

        参数:
            text (str): 待编码的文本字符串

        返回:
            list[int]: 整数 ID 列表
        """
        # 使用正则表达式分割文本
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        # 清理分词结果
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]

        # 将每个 token 映射为对应的整数 ID
        ids = [self.str_to_int[token] for token in preprocessed]
        return ids

    def decode(self, ids):
        """
        解码方法：将整数 ID 序列还原为文本

        参数:
            ids (list[int]): 整数 ID 列表

        返回:
            str: 解码后的文本字符串
        """
        # 将整数 ID 列表转换为字符串列表，然后用空格连接
        text = ' '.join([self.int_to_str[i] for i in ids])

        # 去除标点符号前的多余空格
        # 例如: "hello , world !" -> "hello, world!"
        text = re.sub(r'\s+([,.:;?_!"()\'])', r'\1', text)
        return text

# 第⑤步：测试分词器

# 创建分词器实例
tokenizer = SimpleTokenizerV1(vocab)

# 测试文本
test_text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""

# 编码
ids = tokenizer.encode(test_text)
print(f"测试文本: {test_text}")
print(f"编码后的 IDs: {ids}")
print(f"IDs 数量: {len(ids)}")

# 解码
decoded_text = tokenizer.decode(ids)
print(f"解码后的文本: {decoded_text}")

# 验证编解码的一致性
print(f"\n编解码是否一致: {test_text == decoded_text}")
