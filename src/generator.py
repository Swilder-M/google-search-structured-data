"""OpenAI API 调用模块"""
import json
import os
import requests
from datetime import datetime
from typing import Optional, Dict, Any
from .config import Config
from .utils import clean_json_response


def load_system_prompt() -> str:
    """
    从文件加载系统提示词并注入当前时间

    Returns:
        系统提示词字符串
    """
    prompt_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'prompts',
        'system_prompt.txt'
    )

    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt_template = f.read()

        # 获取当前UTC时间
        current_time_utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

        # 替换时间占位符
        prompt = prompt_template.replace('{{CURRENT_TIME_UTC}}', current_time_utc)

        return prompt
    except (FileNotFoundError, IOError) as e:
        print(f'Error loading system prompt: {e}')
        return ''


def generate_structured_data(url: str, content: str) -> Optional[Dict[str, Any]]:
    """
    使用 OpenAI API 生成结构化数据

    Args:
        url: 页面URL
        content: 页面内容(markdown格式)

    Returns:
        生成的结构化数据字典,失败返回None
    """
    # 验证配置
    try:
        Config.validate()
    except ValueError as e:
        print(f'Configuration error: {e}')
        return None

    # 加载系统提示词
    system_prompt = load_system_prompt()
    if not system_prompt:
        print('Failed to load system prompt')
        return None

    # 构建用户提示
    user_prompt = f'''Generate Google structured data (JSON-LD) for the following webpage.

URL: {url}

Content:
{content}

Analyze the content carefully and generate the most appropriate schema.org structured data. Remember to:
1. Base all information ONLY on the provided content
2. Select schema type(s) that match the content purpose
3. DO NOT fabricate information not present in the content
4. Use the provided URL in appropriate fields'''

    # 准备 API 请求
    api_url = f'{Config.OPENAI_API_BASE}/chat/completions'

    headers = {
        'Authorization': f'Bearer {Config.OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': Config.OPENAI_MODEL,
        'temperature': 0.3,
        'messages': [
            {'role': 'system', 'content': system_prompt.strip()},
            {'role': 'user', 'content': user_prompt.strip()}
        ]
    }

    # 发送请求
    try:
        print('Calling OpenAI API...')
        response = requests.post(api_url, headers=headers, json=data, timeout=120)
        response.raise_for_status()

        # 解析响应
        response_data = response.json()
        generated_content = response_data['choices'][0]['message']['content'].strip()

        # 清理并解析 JSON
        cleaned_content = clean_json_response(generated_content)
        structured_data = json.loads(cleaned_content)

        print('✓ Structured data generated successfully')
        return structured_data

    except requests.RequestException as e:
        print(f'Error calling OpenAI API: {e}')
        if hasattr(e, 'response') and e.response is not None:
            print(f'Response: {e.response.text}')
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f'Error parsing API response: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

    return None
