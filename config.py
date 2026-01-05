"""配置管理模块"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """应用配置类"""
    
    # h2ogpte 配置
    H2OGPTE_BASE_URL: str = os.getenv("H2OGPTE_BASE_URL", "https://h2ogpte.genai.h2o.ai")
    H2OGPTE_SESSION: str = os.getenv("H2OGPTE_SESSION", "")
    H2OGPTE_CSRF_TOKEN: str = os.getenv("H2OGPTE_CSRF_TOKEN", "")
    # 默认为 h2ogpte-guest，登录用户需要设置为 workspaces/<uuid>
    H2OGPTE_WORKSPACE_ID: str = os.getenv("H2OGPTE_WORKSPACE_ID", "workspaces/h2ogpte-guest")
    # 自定义 Prompt Template ID（留空则不使用，填写 UUID 如：37b22dcd-a3c7-406c-8890-387ea6668513）
    H2OGPTE_PROMPT_TEMPLATE_ID: str = os.getenv("H2OGPTE_PROMPT_TEMPLATE_ID", "")
    
    # 服务器配置
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "2156"))
    
    # API Key 验证（留空则不验证）
    API_KEY: str = os.getenv("API_KEY", "")
    
    # API 端点
    RPC_ENDPOINT: str = f"{H2OGPTE_BASE_URL}/rpc/db"
    
    @classmethod
    def get_cookies(cls) -> dict:
        """获取请求所需的 cookies"""
        return {
            "h2ogpte.session": cls.H2OGPTE_SESSION
        }
    
    @classmethod
    def get_headers(cls) -> dict:
        """获取请求所需的 headers"""
        return {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": cls.H2OGPTE_BASE_URL,
            "x-csrf-token": cls.H2OGPTE_CSRF_TOKEN,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }


config = Config()
