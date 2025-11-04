"""Google 结构化数据验证器

支持: WebPage, FAQPage, Article, Organization
参考: https://developers.google.com/search/docs/appearance/structured-data/
"""
from typing import Dict, Any, Optional


class StructuredDataValidator:
    """结构化数据验证器"""

    # 必需的字段
    REQUIRED_FIELDS = ['@context', '@type']

    # 支持的 @type 类型
    SUPPORTED_TYPES = [
        'WebPage',
        'FAQPage',
        'Article',
        'Organization',
        'SoftwareApplication',  # 软件产品
        'Question',  # FAQ 使用
        'Answer',  # FAQ 使用
        'ImageObject',  # 辅助类型
        'ContactPoint',  # Organization 使用
    ]

    @classmethod
    def validate(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证结构化数据是否符合 schema.org 规范

        Args:
            data: 待验证的结构化数据

        Returns:
            (是否有效, 错误信息)
        """
        # 检查是否为字典
        if not isinstance(data, dict):
            return False, 'Structured data must be a dictionary'

        # 检查必需字段
        for field in cls.REQUIRED_FIELDS:
            if field not in data:
                return False, f'Missing required field: {field}'

        # 验证 @context
        if not cls._validate_context(data.get('@context')):
            return False, 'Invalid @context, must be "https://schema.org"'

        # 验证 @type
        schema_type = data.get('@type')
        if not cls._validate_type(schema_type):
            return (
                False,
                f'Unsupported @type: {schema_type}. Supported types: WebPage, FAQPage, Article, Organization'
            )

        # 根据不同类型进行特定验证
        if schema_type == 'WebPage':
            return cls._validate_web_page(data)
        elif schema_type == 'FAQPage':
            return cls._validate_faq_page(data)
        elif schema_type == 'Article':
            return cls._validate_article(data)
        elif schema_type == 'Organization':
            return cls._validate_organization(data)
        elif schema_type == 'SoftwareApplication':
            return cls._validate_software_application(data)

        # 对于其他辅助类型,只要有必需字段就通过
        return True, None

    @staticmethod
    def _validate_context(context: Any) -> bool:
        """验证 @context 字段"""
        return context == 'https://schema.org'

    @classmethod
    def _validate_type(cls, schema_type: Any) -> bool:
        """验证 @type 字段"""
        if isinstance(schema_type, str):
            return schema_type in cls.SUPPORTED_TYPES
        elif isinstance(schema_type, list):
            return all(t in cls.SUPPORTED_TYPES for t in schema_type)
        return False

    @classmethod
    def _validate_web_page(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证 WebPage 类型

        必需字段:
        - name: 页面标题
        - description: 页面描述
        - url: 页面URL
        """
        required_fields = ['name', 'description', 'url']

        for field in required_fields:
            if field not in data:
                return False, f'WebPage must have {field} field'

        # 如果有 keywords,验证其为数组
        if 'keywords' in data:
            keywords = data['keywords']
            if not isinstance(keywords, list):
                return False, 'WebPage keywords must be an array'
            if not all(isinstance(k, str) for k in keywords):
                return False, 'WebPage keywords must be an array of strings'

        # 如果有 mainEntity,验证其为 FAQPage
        if 'mainEntity' in data:
            main_entity = data['mainEntity']
            if not isinstance(main_entity, dict):
                return False, 'WebPage mainEntity must be a dictionary'

            if main_entity.get('@type') == 'FAQPage':
                # 验证嵌套的 FAQPage
                is_valid, error = cls._validate_faq_page(main_entity)
                if not is_valid:
                    return False, f'Invalid mainEntity FAQPage: {error}'

        return True, None

    @classmethod
    def _validate_faq_page(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证 FAQPage 类型

        必需字段:
        - mainEntity: Question 数组
        """
        if 'mainEntity' not in data:
            return False, 'FAQPage must have mainEntity field'

        main_entity = data['mainEntity']
        if not isinstance(main_entity, list):
            return False, 'FAQPage mainEntity must be a list'

        if len(main_entity) == 0:
            return False, 'FAQPage mainEntity must contain at least one Question'

        # 验证每个问题
        for i, question in enumerate(main_entity):
            if not isinstance(question, dict):
                return False, f'Question {i + 1} must be a dictionary'

            if question.get('@type') != 'Question':
                return False, f'Question {i + 1} must have @type: "Question"'

            if 'name' not in question:
                return False, f'Question {i + 1} must have "name" field (the question text)'

            # 验证答案
            answer = question.get('acceptedAnswer')
            if not answer:
                return False, f'Question {i + 1} must have "acceptedAnswer" field'

            if not isinstance(answer, dict):
                return False, f'Question {i + 1} acceptedAnswer must be a dictionary'

            if answer.get('@type') != 'Answer':
                return False, f'Question {i + 1} acceptedAnswer must have @type: "Answer"'

            if 'text' not in answer:
                return False, f'Question {i + 1} answer must have "text" field'

        return True, None

    @classmethod
    def _validate_article(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证 Article 类型

        必需字段:
        - headline: 文章标题
        - author: 作者信息
        - datePublished: 发布日期
        - dateModified: 修改日期
        """
        required_fields = ['headline', 'author']

        for field in required_fields:
            if field not in data:
                return False, f'Article must have {field} field'

        # 验证 author 字段
        author = data['author']
        if not isinstance(author, dict):
            return False, 'Article author must be a dictionary'

        if '@type' not in author or author['@type'] not in ['Person', 'Organization']:
            return False, 'Article author must have @type: "Person" or "Organization"'

        if 'name' not in author:
            return False, 'Article author must have name field'

        return True, None

    @classmethod
    def _validate_organization(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证 Organization 类型

        必需字段:
        - name: 组织名称

        推荐字段:
        - contactPoint: 联系方式数组
        """
        if 'name' not in data:
            return False, 'Organization must have name field'

        # 如果有 contactPoint,验证其结构
        if 'contactPoint' in data:
            contact_points = data['contactPoint']
            if not isinstance(contact_points, list):
                return False, 'Organization contactPoint must be an array'

            for i, contact in enumerate(contact_points):
                if not isinstance(contact, dict):
                    return False, f'ContactPoint {i + 1} must be a dictionary'

                if contact.get('@type') != 'ContactPoint':
                    return False, f'ContactPoint {i + 1} must have @type: "ContactPoint"'

                if 'contactType' not in contact:
                    return False, f'ContactPoint {i + 1} must have contactType field'

        return True, None

    @classmethod
    def _validate_software_application(cls, data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        验证 SoftwareApplication 类型

        必需字段:
        - name: 应用名称

        推荐字段:
        - description: 应用描述
        - url: 应用URL
        - applicationCategory: 应用分类 (必须与 operatingSystem 同时存在)
        - operatingSystem: 支持的操作系统 (必须与 applicationCategory 同时存在)
        - featureList: 功能列表
        - manufacturer: 制造商
        - keywords: 关键词数组
        """
        # 必需字段
        if 'name' not in data:
            return False, 'SoftwareApplication must have name field'

        # 验证 applicationCategory 和 operatingSystem 必须同时存在
        has_app_category = 'applicationCategory' in data
        has_operating_system = 'operatingSystem' in data

        if has_app_category and not has_operating_system:
            return False, 'SoftwareApplication with applicationCategory must also have operatingSystem field'

        if has_operating_system and not has_app_category:
            return False, 'SoftwareApplication with operatingSystem must also have applicationCategory field'

        # 验证 applicationCategory 格式
        if has_app_category:
            app_category = data['applicationCategory']
            if not isinstance(app_category, str):
                return False, 'SoftwareApplication applicationCategory must be a string'
            if app_category not in ['BusinessApplication', 'DeveloperApplication', 'UtilitiesApplication']:
                return False, 'SoftwareApplication applicationCategory must be one of: BusinessApplication, DeveloperApplication, UtilitiesApplication'

        # 验证 operatingSystem 格式
        if has_operating_system:
            operating_system = data['operatingSystem']
            if not isinstance(operating_system, str):
                return False, 'SoftwareApplication operatingSystem must be a string'

        # 如果有 featureList,验证其为数组
        if 'featureList' in data:
            features = data['featureList']
            if not isinstance(features, list):
                return False, 'SoftwareApplication featureList must be an array'
            if not all(isinstance(f, str) for f in features):
                return False, 'SoftwareApplication featureList must be an array of strings'

        # 如果有 keywords,验证其为数组
        if 'keywords' in data:
            keywords = data['keywords']
            if not isinstance(keywords, list):
                return False, 'SoftwareApplication keywords must be an array'
            if not all(isinstance(k, str) for k in keywords):
                return False, 'SoftwareApplication keywords must be an array of strings'

        # 如果有 manufacturer,验证其为 Organization
        if 'manufacturer' in data:
            manufacturer = data['manufacturer']
            if not isinstance(manufacturer, dict):
                return False, 'SoftwareApplication manufacturer must be a dictionary'

            if manufacturer.get('@type') != 'Organization':
                return False, 'SoftwareApplication manufacturer must have @type: "Organization"'

            if 'name' not in manufacturer:
                return False, 'SoftwareApplication manufacturer must have name field'

        return True, None
