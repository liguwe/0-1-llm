# %% [markdown]
# # 第二章：文本数据处理

# %%

############################################################################
# ① 环境检查，打印 PyTorch 和 tiktoken 的安装版本
############################################################################

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
# %% 

############################################################################
# ② 为了训练大模型，选择短篇小说 The Verdict 作为分词文本
############################################################################

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
        # 读取文件的全部内容并存储在 text 变量中
        # 指定 encoding="utf-8" 确保正确处理 UTF-8 编码的文本
        text = f.read()
    
    # 打印文本的前 1000 个字符，用于快速预览文件内容是否正确加载
    print(text[:1000])
else:
    # 如果文件已存在，则直接读取本地文件
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
# %%
