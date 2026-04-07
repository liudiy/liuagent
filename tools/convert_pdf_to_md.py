import os
import glob
import sys

def convert_pdfs_in_directory(input_dir, output_dir):
    """
    遍历指定目录下的所有 PDF 文件，并将其转换为 Markdown 格式。
    优先尝试使用 pymupdf4llm (效果最好，支持表格和排版)，
    如果未安装，则回退使用基础的 fitz (PyMuPDF)。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    pdf_files = glob.glob(os.path.join(input_dir, "**", "*.pdf"), recursive=True)
    
    if not pdf_files:
        print(f"⚠️ 在 {input_dir} 及其子目录中没有找到任何 PDF 文件。")
        return

    print(f"🔍 找到 {len(pdf_files)} 个 PDF 文件，准备开始转换...")

    # 尝试导入高级转换库
    try:
        import pymupdf4llm
        has_pymupdf4llm = True
        print("✅ 检测到 pymupdf4llm，将使用高级 Markdown 提取引擎。")
    except ImportError:
        has_pymupdf4llm = False
        print("⚠️ 未检测到 pymupdf4llm，将回退使用基础 PyMuPDF 提取纯文本。")
        print("💡 强烈建议执行: pip install pymupdf4llm 获取更好的表格和标题排版效果。")
        try:
            import fitz
        except ImportError:
            print("❌ 连基础的 PyMuPDF (fitz) 都没有安装。请执行: pip install pymupdf")
            sys.exit(1)

    for pdf_path in pdf_files:
        # 保持原始的相对目录结构
        rel_path = os.path.relpath(pdf_path, input_dir)
        base_name = os.path.splitext(rel_path)[0]
        md_path = os.path.join(output_dir, f"{base_name}.md")
        
        # 确保输出子目录存在
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        
        print(f"🔄 正在转换: {os.path.basename(pdf_path)} -> {os.path.basename(md_path)}")
        
        try:
            if has_pymupdf4llm:
                # 高级提取：带表格、标题、列表等 Markdown 格式
                try:
                    md_text = pymupdf4llm.to_markdown(pdf_path)
                except Exception as inner_e:
                    if "ONNXRuntimeError" in str(inner_e):
                        print(f"  ⚠️ pymupdf4llm 发生 ONNX 类型错误，自动降级为基础提取: {str(inner_e)}")
                        import fitz
                        doc = fitz.open(pdf_path)
                        md_text = ""
                        for page_num in range(len(doc)):
                            page = doc.load_page(page_num)
                            md_text += f"## 第 {page_num + 1} 页\n\n"
                            md_text += page.get_text("text") + "\n\n"
                        doc.close()
                    else:
                        raise inner_e
                
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(md_text)
            else:
                # 基础提取：纯文本转存为 .md
                doc = fitz.open(pdf_path)
                with open(md_path, "w", encoding="utf-8") as f:
                    for page_num in range(len(doc)):
                        page = doc.load_page(page_num)
                        text = page.get_text("text")
                        f.write(f"## 第 {page_num + 1} 页\n\n")
                        f.write(text)
                        f.write("\n\n")
                doc.close()
            print(f"  ✔️ 转换成功!")
        except Exception as e:
            print(f"  ❌ 转换失败 {pdf_path}: {str(e)}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="批量将 PDF 转换为 Markdown 以供 Agentic RAG 使用")
    parser.add_argument("--input", "-i", type=str, default="./TongData", help="包含 PDF 的输入目录")
    parser.add_argument("--output", "-o", type=str, default="./TongData_MD", help="输出 Markdown 的目录")
    
    args = parser.parse_args()
    
    input_directory = os.path.abspath(args.input)
    output_directory = os.path.abspath(args.output)
    
    print(f"📥 输入目录: {input_directory}")
    print(f"📤 输出目录: {output_directory}")
    
    convert_pdfs_in_directory(input_directory, output_directory)
    print("\n🎉 所有转换任务完成！Agent 现在可以使用文件系统工具探索这些 Markdown 文件了。")
