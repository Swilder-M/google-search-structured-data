"""工具函数模块"""
import json
from typing import Optional


def read_markdown_file(file_path: str) -> Optional[str]:
    """
    读取 Markdown 文件内容

    Args:
        file_path: 文件路径

    Returns:
        文件内容,失败返回None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, IOError) as e:
        print(f'Error reading file {file_path}: {e}')
        return None


def save_json_output(data: dict, output_path: str) -> bool:
    """
    保存JSON数据到文件

    Args:
        data: 要保存的数据
        output_path: 输出文件路径

    Returns:
        是否成功
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except (IOError, TypeError) as e:
        print(f'Error saving JSON to {output_path}: {e}')
        return False


def clean_json_response(content: str) -> str:
    """
    清理 OpenAI 返回的 JSON 内容,去除 markdown 代码块标记

    Args:
        content: 原始内容

    Returns:
        清理后的内容
    """
    content = content.strip()

    # 移除 markdown 代码块标记
    if content.startswith('```json'):
        content = content[7:]
    elif content.startswith('```'):
        content = content[3:]

    if content.endswith('```'):
        content = content[:-3]

    return content.strip()
