# %% [markdown]
# # 第二章：文本数据处理

# %% ① 环境检查，打印 PyTorch 和 tiktoken 的安装版本


# 从 importlib.metadata 模块导入 version 函数，用于查询已安装包的版本号
from importlib.metadata import version

# 导入 PyTorch 深度学习框架
import torch

# 导入 tiktoken 分词器库，用于将文本转换为 token 序列
import tiktoken

# 打印 PyTorch 的安装版本，确保深度学习框架正确安装并识别版本
print("torch version:", version("torch"))

# 打印 tiktoken 的安装版本，确保分词器库正确安装并识别版本
print("tiktoken version:", version("tiktoken"))
# %% ② 为了训练大模型，选择短篇小说 The Verdict 作为分词文本

# 导入 os 模块，用于操作系统相关操作（如检查文件是否存在）
import os

# 导入 requests 库，用于发送 HTTP 请求并下载网络资源
import requests

# 检查本地是否已经存在 "the-verdict.txt" 文件，避免重复下载
if not os.path.exists("the-verdict.txt"):
    # 定义文本文件的下载 URL，来自 GitHub 仓库 "LLMs-from-scratch"
    # 使用 raw.githubusercontent.com 确保下载的是纯文本内容，而非 HTML 页面
    # 这是一个经过精心准备的公开资源，用于深度学习课程
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"
    
    # 定义本地文件保存路径
    file_path = "the-verdict.txt"

    # 发送 GET 请求下载文件，timeout=30 表示最长等待 30 秒
    # 防止网络连接缓慢导致程序长时间等待
    response = requests.get(url, timeout=30)
    
    # 检查 HTTP 响应状态码，如果是 4xx 或 5xx 错误则抛出异常
    response.raise_for_status()
    
    # 以二进制写入模式 "wb" 打开文件
    # "wb" 模式用于写入二进制数据，防止文本编码问题
    with open(file_path, "wb") as f:
        # 将响应体的原始二进制内容（response.content）写入文件
        # 相比 response.text，这样做更安全，保留原始编码
        f.write(response.content)

    # 以文本读取模式 "r" 打开文件，读取文本内容
    with open(file_path, "r", encoding="utf-8") as f: 
        # 读取文件的全部内容并存储在 raw_text 变量中
        # 指定 encoding="utf-8" 确保正确处理 UTF-8 编码的文本
        raw_text = f.read()
    
    # 打印文本的前 1000 个字符，用于快速预览文件内容是否正确加载
    print(raw_text[:1000])
else:
    # 如果文件已存在，则直接读取本地文件
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    # 打印文本的前 1000 个字符，用于快速预览文件内容是否正确加载
    print(raw_text[:1000])
    
# %% ③ 使用正则表达式进行基础分词（Tokenization）

import re  

# 示例：使用简单文本演示分词效果
sample_text = "Hello, do you like tea?"  
sample_preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', sample_text)  
# item.strip() - 去除字符串两端的空白字符（空格、制表符、换行符等）
sample_preprocessed = [item.strip() for item in sample_preprocessed if item.strip()]  
print("示例分词结果:", sample_preprocessed)  

# %% ④ 打印小说文本的前 1000 个字符

# 使用正则表达式对小说文本进行分词
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

print("分词后的前 100 个 token:", preprocessed[:99])

print("分词后的文本长度:", len(preprocessed))

# %% ⑤ 建立词汇表，只是使用了部分数据，展示逻辑

# 这里模拟一部分数据，展示逻辑
preprocessed_part = ['I', 'HAD', 'always', 'thought', 'Jack', 'Gisburn', '...']

# 1. 去重：使用 set 去掉重复单词
# 2. 排序：使用 sorted 按字母顺序排列
all_words_part = sorted(list(set(preprocessed_part)))

# 3. 查看词汇表大小
vocab_size_part = len(all_words_part)
print("排序去重后的词汇表:", all_words_part)
print("排序去重后的词汇表大小:", vocab_size_part)

# 4. 创建字典：{单词: 整数ID}
vocab_part = {token: integer for integer, token in enumerate(all_words_part)}


# 打印前 5 个看看长什么样
for i, item in enumerate(vocab_part.items()):
    print(item)
    if i >= 5:
        break
# %% 分词器 SimpleTokenizerV1 

# 导入正则表达式模块，用于文本分割和替换操作
import re

# SimpleTokenizerV1: 简单的文本分词器（第一版）
# 功能：将文本转换为整数 ID 序列（编码），以及将整数 ID 序列还原为文本（解码）
# 这是构建大语言模型（LLM）的基础组件之一
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
        self.int_to_str = {i:s for s,i in vocab.items()}
        
    def encode(self, text):
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
        
    def decode(self, ids):
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

        # 列表推导式，对比 JavaScript，如下
        # 对比 const text = ids.map(i => self.int_to_str[i]).join(" ");

        # 用于从一个可迭代对象（如列表）创建另一个新列表
        text = ' '.join([self.int_to_str[i] for i in ids])

        # 去除标点符号前的多余空格
        # 正则表达式说明:
        # - r'\s+([,.:;?_!"()\'])': 匹配"一个或多个空白字符 + 标点符号"
        # - r'\1': 替换为第一个捕获组（即标点符号本身），去掉前面的空格
        # 例如: "hello , world !" -> "hello, world!"
        # 对比 JavaScript → text.replace(/\s+([,.:;?_!"()\'])/g, "$1");
        # 三个参数说明
        # - r'\s+([,.:;?_!"()\'])': 匹配模式
        # - r'\1': 需要替换为的模式，\1 表示第一个捕获组, 'r' 代表原始字符串
        # - text: 输入字符串，即目标字符串
        text = re.sub(r'\s+([,.:;?_!"()\'])', r'\1', text)
        return text 


# %% ⑥ 测试分词器

# 确保 preprocessed 变量已定义（防止在交互式模式下漏跑之前的 Cell）
if "preprocessed" not in locals():
    # 如果没跑之前的代码，这里重新简单处理一下 raw_text
    # 假设 raw_text 在前面的 Cell 里已经读取成功
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(list(set(preprocessed)))
vocab = {token: integer for integer, token in enumerate(all_words)}
tokenizer = SimpleTokenizerV1(vocab)

test_text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(test_text)
print('ids:', ids)

decoded_text = tokenizer.decode(ids)
print('text:', decoded_text)

# %%

