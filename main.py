#!/usr/bin/env python3
"""
Google Structured Data Generator

生成 Google 结构化数据(JSON-LD)的工具脚本
"""
import sys
import os
import json
from datetime import datetime
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.config import Config
from src.utils import read_markdown_file, save_json_output
from src.generator import generate_structured_data
from src.validator import StructuredDataValidator


def main():
    """主函数"""
    print('=' * 60)
    print('Google Structured Data Generator')
    print('=' * 60)
    print()

    # 检查命令行参数
    if len(sys.argv) < 3:
        print('Usage: python main.py <url> <markdown_file1> [markdown_file2] ...')
        print()
        print('Example:')
        print('  python main.py https://www.emqx.com/en/solutions/industries/automotive tests/automotive.md')
        print()
        sys.exit(1)

    # 获取参数
    url = sys.argv[1]
    markdown_files = sys.argv[2:]

    print(f'URL: {url}')
    print(f'Markdown files: {", ".join(markdown_files)}')
    print()

    # 验证配置
    try:
        Config.validate()
        print('✓ Configuration validated')
    except ValueError as e:
        print(f'✗ Configuration error: {e}')
        sys.exit(1)

    # 读取所有 markdown 文件内容
    all_content = []
    for md_file in markdown_files:
        if not os.path.exists(md_file):
            print(f'✗ File not found: {md_file}')
            sys.exit(1)

        print(f'Reading {md_file}...')
        content = read_markdown_file(md_file)
        if content is None:
            print(f'✗ Failed to read {md_file}')
            sys.exit(1)

        all_content.append(content)
        print(f'✓ Read {len(content)} characters from {md_file}')

    # 合并所有内容
    combined_content = '\n\n---\n\n'.join(all_content)
    print()
    print(f'Total content: {len(combined_content)} characters')
    print()

    # 生成结构化数据
    print('Generating structured data...')
    structured_data = generate_structured_data(url, combined_content)

    if structured_data is None:
        print('✗ Failed to generate structured data')
        sys.exit(1)

    print()
    print('Generated structured data:')
    print(json.dumps(structured_data, ensure_ascii=False, indent=2))
    print()

    # 验证结构化数据
    print('Validating structured data...')
    is_valid, error_message = StructuredDataValidator.validate(structured_data)

    if not is_valid:
        print(f'✗ Validation failed: {error_message}')
        print()
        print('The generated data does not meet schema.org requirements.')
        sys.exit(1)

    print('✓ Validation passed')
    print()

    # 保存输出文件
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'structured_data_{timestamp}.json'
    output_path = os.path.join('output', output_filename)

    # 确保输出目录存在
    os.makedirs('output', exist_ok=True)

    if save_json_output(structured_data, output_path):
        print(f'✓ Saved to {output_path}')
    else:
        print(f'✗ Failed to save output file')
        sys.exit(1)

    print()
    print('=' * 60)
    print('Success! Structured data generated and validated.')
    print('=' * 60)


if __name__ == '__main__':
    main()
