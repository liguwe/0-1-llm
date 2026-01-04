# tokenizer_class.py 详解

> **步骤 5: 实现分词器类（Tokenizer Class）**

## 📝 功能说明

创建可复用的 `SimpleTokenizerV1` 类，提供 `encode()`（文本→ID）和 `decode()`（ID→文本）方法。

---

## 🔍 核心概念

### 1. 类（Class）定义

#### Python 实现
```python
class SimpleTokenizerV1:
    """简单分词器 V1 版本"""

    def __init__(self, vocab: Dict[str, int]):
        """初始化分词器"""
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}
```

#### JavaScript/TypeScript 等价实现
```typescript
class SimpleTokenizerV1 {
  private strToInt: Map<string, number>;
  private intToStr: Map<number, string>;

  constructor(vocab: Record<string, number>) {
    // 保存原始词汇表
    this.strToInt = new Map(Object.entries(vocab).map(([k, v]) => [k, v]));

    // 创建反向映射
    this.intToStr = new Map(Object.entries(vocab).map(([k, v]) => [v, k]));
  }

  encode(text: string): number[] {
    // 编码逻辑
    return [];
  }

  decode(ids: number[]): string {
    // 解码逻辑
    return "";
  }
}
```

**类的基本语法：**

```python
class MyClass:
    """类文档字符串"""

    # 类属性（所有实例共享）
    class_attr = "I am shared"

    def __init__(self, value):
        """构造方法"""
        # 实例属性（每个实例独立）
        self.instance_attr = value

    def method(self):
        """实例方法"""
        return self.instance_attr

# 使用
obj = MyClass("hello")
print(obj.method())  # "hello"
```

---

### 2. __init__ 构造方法

#### Python 实现
```python
def __init__(self, vocab: Dict[str, int]):
    """初始化分词器"""
    self.str_to_int = vocab
    self.int_to_str = {i: s for s, i in vocab.items()}
```

#### JavaScript 等价实现
```javascript
constructor(vocab) {
  // 初始化
  this.strToInt = vocab;
  this.intToStr = Object.fromEntries(
    Object.entries(vocab).map(([k, v]) => [v, k])
  );
}
```

**__init__ 详解：**

```python
class Person:
    def __init__(self, name, age):
        """创建对象时自动调用"""
        self.name = name
        self.age = age

# 使用
person = Person("Alice", 25)
# __init__ 自动被调用
print(person.name)  # "Alice"
print(person.age)   # 25

# JavaScript 对比
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const person = new Person("Alice", 25);
console.log(person.name);  // "Alice"
```

**关键区别：**
- Python: `__init__(self)` - 初始化已创建的对象
- JavaScript: `constructor()` - 创建并初始化对象

---

### 3. self 关键字

#### Python 实现
```python
class SimpleTokenizerV1:
    def __init__(self, vocab):
        # self 指向当前实例
        self.str_to_int = vocab

    def encode(self, text):
        # self 访问实例属性
        return [self.str_to_int[token] for token in text.split()]
```

#### JavaScript 等价实现
```javascript
class SimpleTokenizerV1 {
  constructor(vocab) {
    // this 指向当前实例
    this.strToInt = vocab;
  }

  encode(text) {
    // this 访问实例属性
    return text.split().map(token => this.strToInt[token]);
  }
}
```

**self vs this：**

| 特性 | Python (self) | JavaScript (this) |
|------|--------------|-----------------|
| 是否必需 | 是（必须显式声明） | 是（隐式） |
| 作为参数 | 第一参数 | 不需要 |
| 指向 | 当前实例 | 取决于调用方式 |
| 箭头函数 | 无 | 绑定外层 this |

**Python 的 self：**

```python
class Example:
    def __init__(self, value):
        self.value = value  # self 必须显式使用

    def show(self):
        # self 必须作为第一个参数
        print(f"Value: {self.value}")

# 调用时不需要传 self
obj = Example(42)
obj.show()  # self 自动绑定到 obj
```

**JavaScript 的 this：**

```javascript
class Example {
  constructor(value) {
    this.value = value;  // this 自动指向实例
  }

  show() {
    console.log(`Value: ${this.value}`);
  }
}

const obj = new Example(42);
obj.show();  // this 自动绑定到 obj
```

---

### 4. 实例方法

#### Python 实现
```python
class SimpleTokenizerV1:
    def encode(self, text: str) -> List[int]:
        """编码方法"""
        # 方法体
        return ids

    def decode(self, ids: List[int]) -> str:
        """解码方法"""
        # 方法体
        return text
```

#### JavaScript 等价实现
```javascript
class SimpleTokenizerV1 {
  encode(text) {
    // 编码方法
    return [];
  }

  decode(ids) {
    // 解码方法
    return "";
  }
}
```

**方法类型对比：**

```python
class Example:
    class_var = "shared"

    def __init__(self):
        self.instance_var = "unique"

    # 实例方法（最常见）
    def instance_method(self):
        return self.instance_var

    # 类方法
    @classmethod
    def class_method(cls):
        return cls.class_var

    # 静态方法
    @staticmethod
    def static_method():
        return "static"

# 使用
obj = Example()
obj.instance_method()  # "unique"
Example.class_method()  # "shared"
Example.static_method()  # "static"
```

```javascript
class Example {
  static classVar = "shared";

  constructor() {
    this.instanceVar = "unique";
  }

  // 实例方法
  instanceMethod() {
    return this.instanceVar;
  }

  // 静态方法
  static staticMethod() {
    return "static";
  }
}

// 使用
const obj = new Example();
obj.instanceMethod();  // "unique"
Example.staticMethod();  // "static"
```

---

### 5. 字符串的 join() 方法

#### Python 实现
```python
# 将整数 ID 列表转换为字符串列表，然后用空格连接
text = ' '.join([self.int_to_str[i] for i in ids])
# 例如: [0, 1, 2] -> ["hello", "world", ","] -> "hello world ,"
```

#### JavaScript 等价实现
```javascript
// 将整数 ID 列表转换为字符串数组，然后用空格连接
const text = ids.map(i => this.intToStr.get(i)).join(' ');
// 例如: [0, 1, 2] -> ["hello", "world", ","] -> "hello world ,"
```

**join() 详解：**

```python
# Python
words = ["Hello", "world", "!"]

# 用空格连接
' '.join(words)  # "Hello world !"

# 用空字符串连接
''.join(words)   # "Helloworld!"

# 用逗号连接
','.join(words)  # "Hello,world,!"

# 用换行符连接
'\n'.join(words)  # "Hello\nworld\n!"
```

```javascript
// JavaScript
const words = ["Hello", "world", "!"];

// 用空格连接
words.join(' ');  // "Hello world !"

// 用空字符串连接
words.join('');   // "Helloworld!"

// 用逗号连接
words.join(',');  // "Hello,world,!"

// 用换行符连接
words.join('\n');  // "Hello\nworld\n!"
```

---

### 6. 正则表达式替换（re.sub）

#### Python 实现
```python
# 去除标点符号前的多余空格
text = re.sub(r'\s+([,.:;?_!"()\'])', r'\1', text)
# "hello , world !" -> "hello, world!"
```

#### JavaScript 等价实现
```javascript
// 去除标点符号前的多余空格
const text = text.replace(/\s+([,.:;?_!"()\'])/g, '$1');
// "hello , world !" -> "hello, world!"
```

**re.sub() 详解：**

```python
import re

text = "Hello, World!"

# 基本替换
re.sub('World', 'Python', text)  # "Hello, Python!"

# 使用正则
re.sub(r'\b[a-z]+\b', 'word', text)  # "word, word!"

# 使用捕获组
re.sub(r'(Hello), (World)', r'\2 and \1', text)  # "World and Hello!"

# 使用函数
def repl(match):
    return match.group(0).upper()

re.sub(r'[a-z]+', repl, text)  # "HELLO, WORLD!"
```

**对比表：**

| 操作 | Python | JavaScript |
|------|--------|-----------|
| 基本替换 | `re.sub(pattern, repl, text)` | `text.replace(pattern, repl)` |
| 全局替换 | 默认全部替换 | 需要 `/g` 标志 |
| 捕获组 | `\1`, `\2` | `$1`, `$2` |
| 使用函数 | `repl` 参数 | 函数作为第二个参数 |

---

### 7. 类型提示（类方法）

#### Python 实现
```python
from typing import List, Dict

class SimpleTokenizerV1:
    def __init__(self, vocab: Dict[str, int]):
        pass

    def encode(self, text: str) -> List[int]:
        pass

    def decode(self, ids: List[int]) -> str:
        pass
```

#### TypeScript 等价实现
```typescript
class SimpleTokenizerV1 {
  constructor(vocab: Record<string, number>) {}

  encode(text: string): number[] {
    return [];
  }

  decode(ids: number[]): string {
    return "";
  }
}
```

---

## 🎯 Python 最佳实践

### 1. 使用属性（@property）

```python
class Tokenizer:
    def __init__(self, vocab):
        self._vocab = vocab

    @property
    def vocab_size(self):
        """只读属性"""
        return len(self._vocab)

# 使用
tokenizer = Tokenizer(vocab)
print(tokenizer.vocab_size)  # 像访问属性一样
# 不是 tokenizer.vocab_size()
```

### 2. 使用 __str__ 和 __repr__

```python
class Tokenizer:
    def __init__(self, vocab):
        self.vocab = vocab

    def __str__(self):
        """面向用户"""
        return f"Tokenizer(vocab_size={len(self.vocab)})"

    def __repr__(self):
        """面向开发者"""
        return f"Tokenizer(vocab={self.vocab})"

# 使用
tokenizer = Tokenizer({"hello": 0})
print(tokenizer)    # Tokenizer(vocab_size=1)
repr(tokenizer)     # Tokenizer(vocab={'hello': 0})
```

---

## 📚 深入理解：分词器设计

### 编码-解码一致性

```python
# 理想情况
text = "Hello, world!"
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)
assert text == decoded  # 应该相等

# 实际情况（可能不一致）
text = "Hello, world!"
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)
# "hello, world!" (大小写可能改变)
```

### 处理未知词（OOV）

```python
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}
        self.unk_id = vocab.get("<UNK>", -1)

    def encode(self, text):
        tokens = text.split()
        ids = []
        for token in tokens:
            if token in self.str_to_int:
                ids.append(self.str_to_int[token])
            elif self.unk_id >= 0:
                ids.append(self.unk_id)
            else:
                raise ValueError(f"Unknown token: {token}")
        return ids
```

---

## 🔄 Python vs JavaScript 完整对比

### 分词器类完整实现

#### Python
```python
import re
from typing import List, Dict

class SimpleTokenizerV1:
    def __init__(self, vocab: Dict[str, int]):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text: str) -> List[int]:
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        tokens = [t.strip() for t in preprocessed if t.strip()]
        return [self.str_to_int[t] for t in tokens]

    def decode(self, ids: List[int]) -> str:
        text = ' '.join([self.int_to_str[i] for i in ids])
        return re.sub(r'\s+([,.:;?_!"()\'])', r'\1', text)
```

#### JavaScript
```javascript
class SimpleTokenizerV1 {
  constructor(vocab) {
    this.strToInt = vocab;
    this.intToStr = Object.fromEntries(
      Object.entries(vocab).map(([k, v]) => [v, k])
    );
  }

  encode(text) {
    const preprocessed = text.split(/([,.:;?_!"()\']|--|\s)/);
    const tokens = preprocessed
      .map(t => t.trim())
      .filter(t => t.length > 0);
    return tokens.map(t => this.strToInt[t]);
  }

  decode(ids) {
    let text = ids.map(i => this.intToStr[i]).join(' ');
    return text.replace(/\s+([,.:;?_!"()\'])/g, '$1');
  }
}
```

---

## 📚 总结

**关键要点：**

1. ✅ **类和对象** - 封装数据和行为
2. ✅ **__init__ 构造方法** - 初始化实例
3. ✅ **self 关键字** - 访问实例属性和方法
4. ✅ **实例方法** - 定义对象行为
5. ✅ **encode/decode** - 分词器的核心功能

**Python vs JavaScript：**
- 类语法相似
- `self` 必须显式声明 vs `this` 隐式
- `__init__` vs `constructor`
- 方法名几乎相同

**推荐阅读：**
- [Python 类文档](https://docs.python.org/3/tutorial/classes.html)
- [OOP 简介](https://realpython.com/python3-object-oriented-programming/)
