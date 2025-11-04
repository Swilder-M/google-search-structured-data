"""配置管理模块"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class Config:
    """应用配置类"""

    # OpenAI API 配置
    OPENAI_API_BASE = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')

    # 验证必需的配置
    @classmethod
    def validate(cls):
        """验证必需的配置项是否存在"""
        if not cls.OPENAI_API_KEY:
            raise ValueError('OPENAI_API_KEY is required in .env file')
        return True
