# main.py 详解

> **步骤 6: 主程序（Main）- 整合所有步骤**

## 📝 功能说明

执行完整的分词器构建流程，整合前面 5 个步骤，从文件下载到分词器测试。

---

## 🔍 核心概念

### 1. 模块导入（Module Import）

#### Python 实现
```python
# 从模块导入函数
from generate_file import generate_file
from read_file import read_file
from tokenization import tokenize
from create_vocab import create_vocab
from tokenizer_class import SimpleTokenizerV1

# 使用
file_path = generate_file()
raw_text = read_file()
```

#### JavaScript 等价实现
```javascript
// ES6 模块导入
import { generateFile } from './generate_file.js';
import { readFile } from './read_file.js';
import { tokenize } from './tokenization.js';
import { createVocab } from './create_vocab.js';
import { SimpleTokenizerV1 } from './tokenizer_class.js';

// 使用
const filePath = generateFile();
const rawText = readFile();

// CommonJS (Node.js)
const { generateFile } = require('./generate_file');
const { readFile } = require('./read_file');
```

**导入方式对比：**

```python
# Python 导入方式

# 1. 导入整个模块
import math
result = math.sqrt(16)

# 2. 导入特定函数
from math import sqrt
result = sqrt(16)

# 3. 导入并重命名
import math as m
result = m.sqrt(16)

# 4. 导入多个
from math import sqrt, pow, log
```

```javascript
// JavaScript 导入方式

// 1. 导入整个模块
import * as math from './math.js';
const result = math.sqrt(16);

// 2. 导入特定函数
import { sqrt } from './math.js';
const result = sqrt(16);

// 3. 导入并重命名
import { sqrt as squareRoot } from './math.js';
const result = squareRoot(16);

// 4. 默认导入
import sqrt from './math.js';
```

---

### 2. main() 函数

#### Python 实现
```python
def main():
    """执行完整的分词器构建流程"""
    # 执行步骤 1-5
    pass

if __name__ == "__main__":
    main()
```

#### JavaScript 等价实现
```javascript
// Node.js (CommonJS)
function main() {
  // 执行步骤
}

if (require.main === module) {
  main();
}

// ES Modules
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);

if (process.argv[1] === __filename) {
  main();
}
```

**为什么需要 main() 函数？**

```python
# ✅ 推荐：使用 main() 函数
def main():
    """主逻辑"""
    setup()
    process()
    cleanup()

if __name__ == "__main__":
    main()  # 直接运行时执行

# 其他文件导入
import my_module
my_module.main()  # 可以手动调用

# ❌ 不推荐：顶层代码
setup()
process()
cleanup()
# 导入时会自动执行，可能不是你想要的
```

---

### 3. 类型提示（返回类型）

#### Python 实现
```python
from typing import None

def print_separator(title: str = "") -> None:
    """打印分隔线"""
    print("\n" + "=" * 70)
    # 不返回任何值
```

#### TypeScript 等价实现
```typescript
function printSeparator(title: string = ""): void {
  console.log("\n" + "=".repeat(70));
  // 不返回任何值
}
```

**None 类型：**

```python
# Python
def func1() -> None:
    """不返回值"""
    print("Hello")

def func2() -> None:
    """返回 None（等价）"""
    print("Hello")
    return None

# 使用
result = func1()  # None
print(result)     # None
```

```javascript
// JavaScript
function func1() {
  console.log("Hello");
  // 不返回值，默认返回 undefined
}

function func2() {
  console.log("Hello");
  return undefined;
}

// 使用
const result = func1();  // undefined
console.log(result);     // undefined
```

---

### 4. 字符串重复操作

#### Python 实现
```python
# 字符串乘法
print("🚀" * 35)  # "🚀🚀🚀...🚀" (35 次)
print("=" * 70)   # "=================================================="
```

#### JavaScript 等价实现
```javascript
// 使用 repeat()
console.log("🚀".repeat(35));
console.log("=".repeat(70));

// 或手动实现
function repeat(str, n) {
  return Array(n + 1).join(str);
}
console.log(repeat("🚀", 35));
```

**Python 字符串操作：**

```python
# 重复
"ha" * 3      # "hahaha"

# 拼接
"hello" + " world"  # "hello world"

# 切片
text = "Hello, World!"
text[0:5]     # "Hello"
text[-6:]     # "World!"

# 格式化
name = "Alice"
f"Hello, {name}"  # "Hello, Alice"
```

---

### 5. 异常处理

#### Python 实现
```python
try:
    main()
except FileNotFoundError as e:
    print(f"\n❌ 错误: {e}")
    print("\n请确保所有步骤文件都在当前目录中")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
```

#### JavaScript 等价实现
```javascript
try {
  main();
} catch (error) {
  if (error.code === 'ENOENT') {
    console.error(`\n❌ 错误: ${error.message}`);
    console.error("\n请确保所有步骤文件都在当前目录中");
    process.exit(1);
  } else {
    console.error(`\n❌ 发生错误: ${error.message}`);
    console.error(error.stack);
    process.exit(1);
  }
}
```

**异常类型：**

```python
# 文件相关异常
FileNotFoundError    # 文件不存在
PermissionError      # 权限不足
IsADirectoryError    # 是目录而非文件

# 其他异常
KeyError             # 字典键不存在
ValueError          # 值错误
TypeError           # 类型错误
```

---

### 6. sys.exit()

#### Python 实现
```python
import sys

# 正常退出
sys.exit(0)

# 异常退出
sys.exit(1)

# 带消息退出
sys.exit("发生错误")
```

#### JavaScript 等价实现
```javascript
// Node.js
process.exit(0);  // 正常退出
process.exit(1);  // 异常退出

// 或抛出错误
throw new Error("发生错误");
```

---

## 🎯 Python 最佳实践

### 1. 组织代码结构

```python
# ✅ 推荐：清晰的步骤分隔
def main():
    # 步骤 1
    print_separator("步骤 1")
    result1 = step1()

    # 步骤 2
    print_separator("步骤 2")
    result2 = step2(result1)

    # 步骤 3
    print_separator("步骤 3")
    result3 = step3(result2)

# ❌ 不推荐：混乱的代码
def main():
    result1 = step1()
    print("---")
    result2 = step2(result1)
    x = step2b()
    result3 = step3(result2, x)
```

### 2. 使用辅助函数

```python
# ✅ 推荐：提取辅助函数
def print_separator(title: str = "") -> None:
    """打印分隔线"""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")

# 使用
print_separator("步骤 1")
print_separator("步骤 2")

# ❌ 不推荐：重复代码
print("\n" + "=" * 70)
print("  步骤 1")
print("=" * 70)
# ... 代码 ...
print("\n" + "=" * 70)
print("  步骤 2")
print("=" * 70)
```

### 3. 错误处理原则

```python
# ✅ 推荐：捕获具体异常
try:
    result = risky_operation()
except SpecificError as e:
    handle_error(e)
except AnotherError as e:
    handle_another(e)

# ❌ 不推荐：捕获所有异常
try:
    result = risky_operation()
except Exception:  # 太宽泛
    pass
```

---

## 📚 深入理解：程序流程

### 完整流程图

```
main()
  │
  ├─> 步骤 1: generate_file()
  │     └─> 下载 the-verdict.txt
  │
  ├─> 步骤 2: read_file()
  │     └─> 读取文件内容
  │
  ├─> 步骤 3: tokenize()
  │     └─> 分词
  │
  ├─> 步骤 4: create_vocab()
  │     └─> 创建词汇表
  │
  ├─> 步骤 5: SimpleTokenizerV1
  │     ├─> encode()
  │     └─> decode()
  │
  └─> 步骤 6: 测试
        ├─> 编码测试
        ├─> 解码测试
        └─> 统计信息
```

---

## 🔄 Python vs JavaScript 完整对比

### 主程序完整实现

#### Python
```python
import sys

def main():
    """主程序"""
    try:
        # 步骤 1-5
        result = step1()
        result = step2(result)
        result = step3(result)
        print("✓ 成功")
    except FileNotFoundError as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### JavaScript
```javascript
async function main() {
  try {
    // 步骤 1-5
    let result = await step1();
    result = await step2(result);
    result = await step3(result);
    console.log("✓ 成功");
  } catch (error) {
    if (error.code === 'ENOENT') {
      console.error(`❌ 错误: ${error.message}`);
      process.exit(1);
    } else {
      console.error(`❌ 未知错误: ${error.message}`);
      process.exit(1);
    }
  }
}

main();
```

---

## 📚 总结

**关键要点：**

1. ✅ **模块导入** - 组织代码结构
2. ✅ **main() 函数** - 程序入口
3. ✅ **异常处理** - 优雅的错误处理
4. ✅ **sys.exit()** - 控制程序退出
5. ✅ **辅助函数** - 提取重复代码

**Python vs JavaScript：**
- 导入语法不同但概念相似
- `if __name__ == "__main__"` vs `require.main === module`
- 异常处理机制相似
- Python 的字符串乘法更简洁

**项目结构总结：**

```
ch02/01/
├── generate_file.py      # 步骤 1: 下载文件
├── read_file.py          # 步骤 2: 读取文件
├── tokenization.py       # 步骤 3: 分词
├── create_vocab.py       # 步骤 4: 创建词汇表
├── tokenizer_class.py    # 步骤 5: 分词器类
├── main.py               # 步骤 6: 主程序
├── README.md             # 项目文档
└── *.md                  # 各文件详解文档
```

**推荐阅读：**
- [Python 模块文档](https://docs.python.org/3/tutorial/modules.html)
- [Python main 函数最佳实践](https://realpython.com/python-main-function/)

---

## 🎓 学习路径建议

1. **先运行代码** - `python main.py` 看效果
2. **逐个阅读** - 从 generate_file.py 到 main.py
3. **理解对比** - 看 Python vs JavaScript 差异
4. **实践修改** - 尝试修改代码，观察变化
5. **扩展功能** - 添加新功能，如重试机制、进度条等

祝学习愉快！🎉
