import os
import base64
from io import BytesIO
from PIL import Image
import fitz  # PyMuPDF, 需要 pip install pymupdf
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 初始化 OpenAI 客户端 (假设使用支持视觉的模型，如 GPT-4o 或 Qwen-VL)
# 注意：如果你使用阿里云的 Qwen-VL，需要替换 base_url 和 api_key
api_key = os.environ.get("DASHSCOPE_API_KEY") # 默认尝试使用 DashScope，如果没有则用 OpenAI
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1" if api_key else None

if not api_key:
    api_key = os.environ.get("OPENAI_API_KEY")
    
if not api_key:
    # 作为一个 fallback 或者为了避免初始化报错
    api_key = "dummy_key"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def pdf_page_to_base64_image(pdf_path: str, page_num: int, zoom: int = 2) -> str:
    """
    使用 PyMuPDF 将 PDF 的特定页转换为 Base64 编码的高清图片。
    zoom: 缩放倍数，2 代表 200% 分辨率（推荐用于 OCR）
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    
    # 设置缩放矩阵提高清晰度
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    # 转换为 PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # 转换为 Base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    doc.close()
    return img_str

def parse_image_to_markdown_with_vlm(base64_image: str) -> str:
    """
    调用视觉大模型 (VLM) 将图片转换为 Markdown。
    """
    system_prompt = """
    你是一个专业的文档解析专家。请将用户提供的文档页面截图，完美转换为 Markdown 格式。
    
    要求：
    1. 准确识别并保留所有的标题层级（使用 #, ##, ###）。
    2. 准确提取正文内容。
    3. 如果图片中包含表格，请使用 Markdown 表格语法完美复刻。
    4. 如果图片中包含控制台截图或代码，请将截图中的关键文字或代码提取出来，放入代码块 (```) 中。
    5. 不要输出任何解释性废话，只输出解析后的 Markdown 文本。
    """
    
    try:
        response = client.chat.completions.create(
            model="qwen-vl-plus", # 默认使用阿里云视觉模型
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "请将这张图片转换为 Markdown。"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=2000,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"VLM 解析失败: {e}")
        return ""

def process_pdf_with_vlm(pdf_path: str, output_md_path: str):
    """
    处理整个 PDF 文件：逐页转图片 -> VLM 解析 -> 拼接保存为 Markdown
    """
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    doc.close()
    
    print(f"开始处理 PDF: {pdf_path} (共 {total_pages} 页)")
    
    full_markdown = ""
    
    for page_num in range(total_pages):
        print(f"正在处理第 {page_num + 1}/{total_pages} 页...")
        
        # 1. 转图片
        base64_img = pdf_page_to_base64_image(pdf_path, page_num)
        
        # 2. VLM 解析
        md_text = parse_image_to_markdown_with_vlm(base64_img)
        
        if md_text:
            full_markdown += f"\n\n<!-- PAGE {page_num + 1} -->\n\n" + md_text
            
    # 3. 保存结果
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(full_markdown)
        
    print(f"✅ 处理完成！Markdown 已保存至: {output_md_path}")
    return full_markdown

if __name__ == "__main__":
    # 测试代码 (需要你提供一个测试 PDF 的路径)
    # test_pdf = "path/to/your/test_manual.pdf"
    # process_pdf_with_vlm(test_pdf, "output_parsed.md")
    print("VLM 解析脚本已就绪。运行前请确保安装了 PyMuPDF 并配置了 VLM 的 API Key。")
