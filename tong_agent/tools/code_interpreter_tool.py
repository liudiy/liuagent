from langchain_core.tools import tool
from e2b_code_interpreter import Sandbox
import os
import base64
import uuid

# 全局的 Sandbox 实例，用于保持代码执行的状态（变量、导入等跨次调用保留）
_global_sandbox = None

def get_or_create_sandbox():
    global _global_sandbox
    # 如果沙箱尚未创建，则初始化一个长生命周期的沙箱
    if _global_sandbox is None:
        import os
        from e2b_code_interpreter import Sandbox
        api_key = os.environ.get("E2B_API_KEY")
        
        # 使用 e2b_code_interpreter 1.0.5 版本
        _global_sandbox = Sandbox(api_key=api_key)
        
        # 启动时将本地的 data 目录同步到沙箱中（供 Agent 分析本地数据）
        local_data_dir = os.path.join(os.getcwd(), "data")
        if os.path.exists(local_data_dir):
            for root, _, files in os.walk(local_data_dir):
                for file in files:
                    local_path = os.path.join(root, file)
                    # 简单映射：统一放入沙箱的 /home/user 目录下
                    remote_path = f"/home/user/{file}"
                    try:
                        with open(local_path, "rb") as f:
                            _global_sandbox.files.write(remote_path, f.read())
                    except Exception as e:
                        print(f"Failed to sync {file} to sandbox: {e}")
                        
    return _global_sandbox

@tool
def python_executor(code: str) -> str:
    """
    当需要进行复杂数学计算、逻辑推演、数据分析、绘制图表或处理文件时，使用此工具。
    输入必须是合法的 Python 代码字符串。
    
    【重要提示】：
    1. 你在一个**有状态**的 Jupyter 环境中运行。之前定义的变量和导入的库在下一次调用中依然有效。
    2. 用户上传的数据文件默认挂载在沙箱的 `/home/user/` 目录下。如果你不知道确切的文件名，或者用户只说了“分析我刚上传的日志”，**请先写代码执行 `import os; print(os.listdir('/home/user/'))` 来查看当前有哪些可用文件，找到目标后再进行分析。** 读取文件时必须使用绝对路径（如 `/home/user/真实文件名.log`）。
    3. 如果你需要生成图表（如使用 matplotlib 画图），**必须直接使用 `plt.show()` 或者将图表对象作为单元格的最后一行直接输出**（不要使用 `plt.savefig` 保存到文件），这样系统会自动捕获图像并返回给你本地的保存路径。
    4. 最好使用 print() 将想要看到的基础文本结果打印出来。
    """
    try:
        # 获取持久化沙箱实例
        sandbox = get_or_create_sandbox()
        
        # 强制检查沙箱是否存活，如果不存活则重新创建
        # 避免 timeout 导致 "The sandbox was not found" 的错误
        # 在 e2b 1.0.5 中没有 is_running 属性，但可以通过捕获执行错误来重试
        
        # 确保本地有 output 目录存放生成的图表
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        
        try:
            execution = sandbox.run_code(code)
        except Exception as e:
            if "not found" in str(e).lower() or "timeout" in str(e).lower():
                # 沙箱可能已经超时销毁，重置并重新创建
                global _global_sandbox
                _global_sandbox = None
                sandbox = get_or_create_sandbox()
                execution = sandbox.run_code(code)
            else:
                raise e
        
        # E2B execution 对象包含了日志、错误和结果
        if execution.error:
            return f"Execution Error:\n{execution.error.name}: {execution.error.value}\n{execution.error.traceback}"
        
        # 收集所有的标准输出（print 的内容）
        logs = []
        for log in execution.logs.stdout:
            logs.append(log)
            
        # 收集最后表达式的直接返回结果及多模态结果（如图表）
        results_text = []
        for result in execution.results:
            if result.text:
                results_text.append(result.text)
                
            # 捕获生成的 PNG 图表
            if hasattr(result, 'png') and result.png:
                try:
                    # 确保是字符串后再 decode
                    png_str = result.png
                    if isinstance(png_str, str):
                        image_data = base64.b64decode(png_str)
                    else:
                        image_data = base64.b64decode(str(png_str))
                    filename = f"chart_{uuid.uuid4().hex[:8]}.png"
                    save_path = os.path.join(output_dir, filename)
                    with open(save_path, "wb") as f:
                        f.write(image_data)
                    results_text.append(f"[系统提示: 成功生成 PNG 图表并已保存至本地: {save_path}]")
                except Exception as e:
                    results_text.append(f"[系统提示: 图片解码保存失败: {str(e)}]")
                
            # 捕获生成的 JPEG 图表
            if hasattr(result, 'jpeg') and result.jpeg:
                image_data = base64.b64decode(result.jpeg)
                filename = f"chart_{uuid.uuid4().hex[:8]}.jpeg"
                save_path = os.path.join(output_dir, filename)
                with open(save_path, "wb") as f:
                    f.write(image_data)
                results_text.append(f"[系统提示: 成功生成 JPEG 图表并已保存至本地: {save_path}]")
        
        final_output = "\n".join(logs + results_text)
        
        return final_output if final_output.strip() else "Code executed successfully, but produced no output. Did you forget to use print() or display()?"
        
    except Exception as e:
        return f"Failed to connect or run in E2B Sandbox: {str(e)}"
