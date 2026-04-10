import os
import re
from pathlib import Path

# 定义要处理的根目录
BASE_DIR = r"C:\Users\79753\OneDrive\Desktop\TongAgent_langgraph\TongData_MD"

def clean_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='gbk') as f:
            lines = f.readlines()

    cleaned_lines = []
    buffer_line = ""

    for line in lines:
        original_line = line
        line = line.strip()
        
        # 1. 过滤掉页码标记和重复的页眉页脚
        if re.match(r'^## 第 \d+ 页$', line):
            continue
        if "版权所有 © 东方通" in line or "东方通负载均衡软件" in line:
            continue
        if "TongWeb" in line and "企业版" in line and "用户手册" in line: # 过滤通用的TongWeb页眉
            continue
        if re.search(r'\.{5,}\s*\d+$', line): # 过滤带大量点和页码的目录行
            continue

        if not line:
            # 遇到空行，把 buffer 里的段落刷入，并保留空行
            if buffer_line:
                cleaned_lines.append(buffer_line)
                buffer_line = ""
            cleaned_lines.append("")
            continue

        # 2. 合并断裂的段落
        # 如果当前行以特定的列表符号开头（如 •, -, 1., 字母.），或者包含 # 标题，或者 buffer 为空，则新起一段
        if (re.match(r'^([•\-*]|\d+\.|[A-Z]\.|#)', line) or 
            line.startswith('|') or # 遇到表格保留
            not buffer_line):
            
            if buffer_line:
                cleaned_lines.append(buffer_line)
            buffer_line = line
        else:
            # 否则，认为它和上一行是同一段落被硬生生切断的，合并它们（加个空格防止英文单词粘连）
            buffer_line += " " + line

    # 刷入最后的内容
    if buffer_line:
        cleaned_lines.append(buffer_line)

    # 覆盖原文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_lines))

def batch_clean_md():
    base_path = Path(BASE_DIR)
    
    if not base_path.exists():
        print(f"错误: 根目录 {base_path} 不存在。")
        return
        
    print(f"\n================ 开始全局清洗: {BASE_DIR} ================")
    
    count = 0
    # 使用 rglob 递归遍历所有子目录下的 .md 文件
    for md_file in base_path.rglob("*.md"):
        print(f"正在清洗: {md_file.relative_to(base_path)}")
        clean_markdown_file(md_file)
        count += 1
        
    print(f"\n完成！成功清洗了总计 {count} 个 Markdown 文件。")

if __name__ == "__main__":
    print("开始执行纯文本正则清洗脚本...")
    batch_clean_md()
    print("\n所有脏 MD 文件清洗完毕，您的 Agent 现在可以畅快搜索了！")
