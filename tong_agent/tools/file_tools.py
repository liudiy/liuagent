import os
import re
import glob
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
            
        flags = re.IGNORECASE if ignore_case else 0
        regex = re.compile(pattern, flags)
        
        results = []
        match_count = 0
        MAX_MATCHES = 150 # Prevent flooding the LLM context
        
        def search_in_file(file_path, rel_path):
            nonlocal match_count
            # Only search in text-like files
            if not file_path.endswith(('.txt', '.md', '.json', '.xml', '.properties', '.conf')):
                return
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        if match_count >= MAX_MATCHES:
                            return
                        # Skip common repetitive PDF headers
                        if "东方通分布式数据缓存中间件软件" in line or "东方通应用服务器软件" in line or "产品用户手册" in line or "服务配置指南" in line or "用户使用手册" in line:
                            continue
                        if regex.search(line):
                            # Clean up line to avoid excessive whitespace
                            clean_line = line.strip()
                            if clean_line:
                                results.append(f"{rel_path}:{i}: {clean_line[:200]}")
                                match_count += 1
            except UnicodeDecodeError:
                # Fallback for gbk if utf-8 fails
                try:
                    with open(file_path, 'r', encoding='gbk') as f:
                        for i, line in enumerate(f, 1):
                            if match_count >= MAX_MATCHES:
                                return
                            if "东方通分布式数据缓存中间件软件" in line or "东方通应用服务器软件" in line or "产品用户手册" in line or "服务配置指南" in line or "用户使用手册" in line:
                                continue
                            if regex.search(line):
                                clean_line = line.strip()
                                if clean_line:
                                    results.append(f"{rel_path}:{i}: {clean_line[:200]}")
                                    match_count += 1
                except Exception:
                    pass # Ignore files that can't be read
            except Exception:
                pass
                
        base_dir = os.path.abspath(os.path.join(os.getcwd(), DATA_DIR))
        
        if os.path.isfile(target_path):
            rel_path = os.path.relpath(target_path, base_dir)
            search_in_file(target_path, rel_path)
        else:
            for root, _, files in os.walk(target_path):
                if match_count >= MAX_MATCHES:
                    break
                for file in files:
                    if match_count >= MAX_MATCHES:
                        break
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, base_dir)
                    search_in_file(file_path, rel_path)
                    
        if not results:
            return f"No matches found for pattern '{pattern}' in {path or 'root'}."
            
        output = "\n".join(results)
        if match_count >= MAX_MATCHES:
            output += f"\n... (Truncated after {MAX_MATCHES} matches. Please refine your search pattern.)"
            
        return output
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
