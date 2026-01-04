# 远程下载文件到本地
import os
import requests

# 获取当前脚本文件所在的绝对目录
# __file__ 是当前文件的路径
# os.path.dirname(__file__) 获取该文件所在的文件夹路径
curr_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_dir, "the-verdict.txt")

print(f"当前工作目录 (CWD): {os.getcwd()}")
print(f"脚本所在目录: {curr_dir}")
print(f"文件将保存至: {file_path}")

# 如果文件不存在，下载文件
if not os.path.exists(file_path):
    print("正在从远程下载...")
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

    # 注意：这是同步阻塞操作，执行完这一行才会跑下一行
    response = requests.get(url) 
    
    if response.status_code == 200:
        # 使用 with 语句打开文件（上下文管理器）
        # 优势：任务完成后会自动关闭文件，即使发生异常也能确保资源释放
        # "as f" 表示将打开的文件对象赋值给变量 f，
        # 这样在缩进块内部就可以通过 f 来操作文件（如 f.write）
        # 类似于js 的  const f = fs.openSync(filePath, "w")
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"下载失败，状态码: {response.status_code}")
    
    # 读取文件内容
    with open(file_path, "r", encoding="utf-8") as f:
        print("下载成功，预览内容：")
        print(f.read()[:200])
else:
    print(f"文件已存在，直接读取...")
    with open(file_path, "r", encoding="utf-8") as f:
        print(f.read()[:200])



