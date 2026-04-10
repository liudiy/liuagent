import os
import glob
import re
import shutil
import subprocess
from typing import Optional
from langchain_core.tools import tool

DATA_DIR = 'TongData_MD'

def _get_absolute_path(path: str) -> str:
    """Helper to safely get absolute path within DATA_DIR"""
    base_dir = os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
    
    # If path is already absolute, ensure it's within base_dir
    if os.path.isabs(path):
        target_path = os.path.abspath(path)
    else:
        # If path is relative to DATA_DIR, e.g., 'subfolder'
        # Or just a filename, e.g., '001_TongWeb.md'
        # Strip leading slashes to prevent os.path.join from treating it as root
        safe_path = path.lstrip('/\\')
        target_path = os.path.abspath(os.path.join(base_dir, safe_path))
        
    if not target_path.startswith(base_dir):
        raise ValueError(f"Path access denied. Must be within {base_dir}")
        
    return target_path

@tool
def list_directory(path: str = "") -> str:
    """
    List files and directories in a specified folder within the knowledge base.
    
    Usage:
    - Use this tool to explore the directory structure of the documentation.
    - Omit 'path' or use "" to list the root knowledge base directory.
    - Provide a relative path like "TongWeb" to list contents of a subfolder.
    
    Returns:
    - A string containing a list of files and directories, one per line.
    """
    try:
        dir_path = _get_absolute_path(path) if path else os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
        
        if not os.path.exists(dir_path):
            return f"Directory {path} does not exist in knowledge base."
            
        if not os.path.isdir(dir_path):
            return f"{path} is a file, not a directory."
            
        entries = os.listdir(dir_path)
        if not entries:
            return f"Directory {path} is empty."
            
        # Format output: directories with trailing slash, files without
        formatted_entries = []
        for entry in entries:
            full_path = os.path.join(dir_path, entry)
            if os.path.isdir(full_path):
                formatted_entries.append(f"{entry}/")
            else:
                formatted_entries.append(entry)
                
        return "\n".join(sorted(formatted_entries))
    except Exception as e:
        return f"Error listing directory: {str(e)}"

@tool
def glob_files(pattern: str) -> str:
    """
    Find files globally using wildcard matching (like '**/*.conf' or '**/*TongWeb*.md').
    
    Usage:
    - Use this to quickly find specific file paths without having to traverse directories manually.
    - Example: `pattern="**/*ssl*"` to find all files containing 'ssl' in their names.
    - Supported wildcards: `*` matches everything, `?` matches any single character, `**` matches multiple directories.
    
    Returns:
    - A string containing a list of matching file paths relative to the knowledge base root.
    """
    try:
        base_dir = os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
        # Navigate to base_dir to make glob patterns relative to it
        original_cwd = os.getcwd()
        os.chdir(base_dir)
        
        try:
            # Use recursive=True to support ** syntax
            matches = glob.glob(pattern, recursive=True)
            
            if not matches:
                return f"No files matched pattern '{pattern}'."
                
            # Filter out directories, only return files
            file_matches = [m for m in matches if os.path.isfile(m)]
            
            if not file_matches:
                return f"Pattern '{pattern}' matched directories, but no files."
                
            return "\n".join(sorted(file_matches))
        finally:
            # Always restore the original working directory
            os.chdir(original_cwd)
            
    except Exception as e:
        return f"Error executing glob: {str(e)}"

@tool
def search_file_content(pattern: str, path: str = "", ignore_case: bool = True) -> str:
    """
    Search for a regular expression pattern within files in the knowledge base (like 'grep').
    
    Usage:
    - Use this to quickly find which files contain specific keywords or configuration names.
    - IMPORTANT: The tool will search all text/markdown files in the specified path.
    - Use multi-word regex like "SSL|TLS|证书|加密" to handle semantic variations.
    
    Args:
    - pattern: The regular expression pattern to search for.
    - path: The file or directory to search in. Defaults to root data dir.
    - ignore_case: Whether to ignore case (default: True).
    
    Returns:
    - A list of matching lines prefixed with the filename and line number.
    """
    try:
        target_path = _get_absolute_path(path) if path else os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
        
        if not os.path.exists(target_path):
            return f"Path {path} does not exist."
            
        # Build the ripgrep command
        # -n: show line numbers
        # -e: pattern
        # --max-columns: limit line length to avoid blowing up context
        # -m: max matches per file (to prevent one file from dominating)
        # --glob: only search text-like files
        # Resolve the actual path of rg to handle Windows PATH issues in subprocess
        rg_path = shutil.which("rg")
        if not rg_path:
            rg_path = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\BurntSushi.ripgrep.MSVC_Microsoft.Winget.Source_8wekyb3d8bbwe\ripgrep-15.1.0-x86_64-pc-windows-msvc\rg.exe")
            if not os.path.exists(rg_path):
                return "Error: 'rg' (ripgrep) command not found on the system. Please ensure ripgrep is installed and in your PATH."

        cmd = [rg_path, "-n", "--max-columns", "250", "-m", "50"]
        
        if ignore_case:
            cmd.append("-i")
            
        cmd.extend(["--glob", "*.{txt,md,json,xml,properties,conf}"])
        cmd.extend(["-e", pattern, target_path])
        
        # Run ripgrep as a subprocess
        # This completely bypasses Python's GIL and runs in true parallel
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            encoding='utf-8', 
            errors='ignore'
        )
        
        if result.returncode == 0:
            # Ripgrep found matches
            output_lines = result.stdout.strip().split('\n')
            base_dir = os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
            
            cleaned_results = []
            match_count = 0
            MAX_MATCHES = 150
            
            for line in output_lines:
                if match_count >= MAX_MATCHES:
                    break
                    
                # Ripgrep output format: /path/to/file:line_number:content
                # We want to make the path relative to base_dir for cleaner output
                if line.startswith(base_dir):
                    line = line[len(base_dir):].lstrip(os.sep)
                    
                # Skip repetitive headers (optional cleanup)
                if "东方通分布式数据缓存中间件软件" in line or "东方通应用服务器软件" in line or "产品用户手册" in line or "服务配置指南" in line or "用户使用手册" in line:
                    continue
                    
                cleaned_results.append(line)
                match_count += 1
                
            final_output = "\n".join(cleaned_results)
            if match_count >= MAX_MATCHES:
                final_output += f"\n\n... (Truncated after {MAX_MATCHES} matches. Please refine your search pattern.)"
            return final_output
            
        elif result.returncode == 1:
            # No matches found
            return f"No matches found for pattern '{pattern}' in {path or 'root'}."
        else:
            # Error occurred (e.g. invalid regex)
            return f"Ripgrep error: {result.stderr}"
            
    except FileNotFoundError:
        return "Error: 'rg' (ripgrep) command not found on the system. Please ensure ripgrep is installed and in your PATH."
    except Exception as e:
        return f"Error searching content: {str(e)}"

@tool
def read_file_content(file_path: str, start_line: int = 1, end_line: int = 500) -> str:
    """
    Read a specific range of lines from a file in the knowledge base (Pagination reading).
    
    Usage:
    - Use this to read the context of a section after locating it via search_file_content.
    - CRITICAL: Never try to read more than 500 lines at once. If the document is large, use pagination!
    - Example: If search results show line 450, read start_line=400 to end_line=500.
    
    Args:
    - file_path: The relative path to the file (e.g., '001_TongWeb.md').
    - start_line: The line number to start reading from (1-indexed, default 1).
    - end_line: The line number to end reading (default 500). Max chunk size is 500 lines.
    
    Returns:
    - The file contents with line numbers.
    """
    try:
        target_path = _get_absolute_path(file_path)
        
        if not os.path.exists(target_path) or not os.path.isfile(target_path):
            return f"File {file_path} does not exist."
            
        # 强制限制最大读取行数，防止 token 溢出
        start_line = max(1, start_line)
        end_line = max(start_line, end_line)
        if end_line - start_line > 500:
            end_line = start_line + 500
        
        lines = []
        try:
            # Try UTF-8 first
            with open(target_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if i < start_line:
                        continue
                    if i > end_line:
                        break
                    lines.append(f"{i:>5} | {line.rstrip()}")
        except UnicodeDecodeError:
            # Fallback to GBK
            lines = []
            with open(target_path, 'r', encoding='gbk') as f:
                for i, line in enumerate(f, 1):
                    if i < start_line:
                        continue
                    if i > end_line:
                        break
                    lines.append(f"{i:>5} | {line.rstrip()}")
                    
        if not lines:
            return f"No content found between lines {start_line}-{end_line}. File might be shorter than {start_line} lines."
            
        result = "\n".join(lines)
        # 如果读取的行数达到了请求的上限，提示还有更多内容
        if len(lines) == (end_line - start_line + 1):
            result += f"\n\n--- End of chunk (Line {end_line}). To read more, call read_file_content with start_line={end_line+1} ---"
            
        return result
    except Exception as e:
        return f"Error reading file: {str(e)}"


