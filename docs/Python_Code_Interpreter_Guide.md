# Python Code Interpreter 核心技术原理与实战指南

本文档旨在拆解 Agent 中 "Code Interpreter" (代码解释器) 的实现原理。我们将从基础概念出发，通过三个循序渐进的实验，带你理解如何让 Python 程序“自己运行自己”。

---

## 1. 核心概念：`exec()` —— 能运行代码的代码

**概念**：
在学校里，你编写 `.py` 文件交给解释器运行。但在 Agent 开发中，LLM 生成的是一段**字符串**形式的代码。`exec()` 函数就是 Python 内置的魔法引擎，它可以把一段字符串当作真正的 Python 代码来执行。

**核心价值**：
赋予 Agent **动态编程能力**。Agent 不再受限于你预先写好的函数，它可以现场编写逻辑来解决未知问题。

**实战实验**：
```python
# 实验 1: 字符串变代码
code_str = "print('Hello from a string!')"
exec(code_str)  # 输出: Hello from a string!

# 实验 2: 动态计算
math_code = "result = 10 * 10; print(f'Result is {result}')"
exec(math_code) # 输出: Result is 100
```

---

## 2. 关键细节：`globals()` —— 代码的生存土壤

**概念**：
`exec(code, globals())` 中的第二个参数 `globals()` 是 Python 的内置函数，它返回当前全局作用域下的所有变量和模块。

**为什么要加它？**
1.  **为了能用 `import`**：没有它，Agent 在代码里写的 `import math` 可能无法正确保存，下一行就用不了。
2.  **为了能用内置函数**：如果你传给 `exec` 一个空字典 `{}`，代码里连 `print()` 都找不到（会报错 `name 'print' is not defined`）。
3.  **为了变量持久化**：多行代码执行时，第一行定义的变量 `x=1` 需要存到一个地方，第二行才能访问到。

**实战实验**：
```python
# 实验 A: 不给土壤（传空字典）-> 报错
try:
    exec("print('Hello')", {})
except Exception as e:
    print(f"实验 A 失败: {e}") 
    # 输出: name 'print' is not defined

# 实验 B: 给足土壤（传 globals()）-> 成功
exec("print('Hello from globals!')", globals())
```

---

## 3. 进阶技巧：`io.StringIO` —— 内存中的“虚拟文件”

**概念**：
通常我们用 `open()` 读写硬盘上的文件。但在高频交互中，写硬盘太慢且不灵活。`io.StringIO` 是一个在**内存**中模拟文件操作的工具。它用起来像文件（有 `write()`, `read()`），但数据只存在于 RAM 中。

**核心价值**：
作为数据缓冲区。在 Code Interpreter 中，我们用它来**暂存**代码执行产生的输出结果。

**实战实验**：
```python
import io

# 创建一个“内存文件”
fake_file = io.StringIO()

# 像写文件一样写入数据
fake_file.write("这是第一行日志\n")
fake_file.write("这是第二行日志")

# 获取所有写入的内容
content = fake_file.getvalue()
print(f"内存文件内容:\n{content}")
```

---

## 3. 高级魔法：`contextlib.redirect_stdout` —— 偷梁换柱

**概念**：
`print()` 函数默认把内容输出到 `sys.stdout`（也就是你的屏幕控制台）。但在 Agent 后台运行代码时，我们不希望结果打印在服务器屏幕上，而是希望**捕获**这些结果并返回给 Agent。`redirect_stdout` 可以在一个 `with` 代码块中，临时把 `print` 的“水管”接到我们指定的对象（如 `StringIO`）上。

**核心价值**：
**捕获输出**。这是 Code Interpreter 能告诉 Agent “刚才代码运行结果是 X” 的关键技术。

**实战实验**：
```python
from contextlib import redirect_stdout
import io

# 1. 准备一个瓶子（内存文件）
capture_buffer = io.StringIO()

print("这行会打印在屏幕上")

# 2. 开始偷梁换柱
with redirect_stdout(capture_buffer):
    print("这行你看不到！因为它被重定向到了 buffer 里")
    print("Agent: 我正在计算...")

# 3. 验证成果
captured_text = capture_buffer.getvalue()
print(f"捕获到的内容: {captured_text}")
```

---

## 4. 综合应用：打造 Code Interpreter 工具

将上述三个技术点结合，就是你在 `code_interpreter.py` 中看到的核心逻辑：

```python
@tool
def execute_python_code(code: str) -> str:
    # 1. 准备瓶子 (StringIO)
    output_buffer = io.StringIO()
    
    try:
        # 2. 偷梁换柱 (redirect_stdout)
        with redirect_stdout(output_buffer):
            # 3. 执行字符串代码 (exec)
            exec(code, globals())
            
        # 4. 返回瓶子里的内容
        return output_buffer.getvalue()
        
    except Exception as e:
        return f"执行出错: {str(e)}"
```

### 学习建议
*   不要死记硬背。
*   **动手敲一遍**上面的三个实验代码。当你亲眼看到 `print` 的内容被“偷”到变量里时，你就彻底掌握了这个知识点。
