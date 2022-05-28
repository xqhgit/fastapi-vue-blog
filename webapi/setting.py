import os
import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from dotenv import dotenv_values

dotenv_config = dotenv_values('.env')


class Settings(BaseSettings):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOG_PATH = os.path.join(BASEDIR, 'logs')
    BACKEND_CORS_ORIGINS: List = ['*']

    # 默认管理员账号密码等信息
    ADMIN_USERNAME = dotenv_config.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = dotenv_config.get('ADMIN_PASSWORD', '123456')
    ADMIN_NICKNAME = dotenv_config.get('ADMIN_NICKNAME', 'admin')
    ADMIN_EMAIL = dotenv_config.get('ADMIN_EMAIL', '1104440778@qq.com')

    # 数据库账号密码
    DB_HOST = dotenv_config.get('DB_HOST', '127.0.0.1')
    DB_PORT = dotenv_config.get('DB_PORT', 3306)
    DB_USER = dotenv_config.get('DB_USER', 'root')
    DB_PASSWORD = dotenv_config.get('DB_PASSWORD', 'fastapivueblog12306')
    DB_NAME = dotenv_config.get('DB_NAME', 'FastAPIVueBlog')

    DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
    SQLALCHEMY_DATABASE_URI: str = f'mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # Elasticsearch
    ELASTIC_HOST = dotenv_config.get('ELASTIC_HOST', '127.0.0.1')
    ELASTIC_PORT = dotenv_config.get('ELASTIC_PORT', 9200)

    # 12 hours
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12
    SECRET_KEY: str = secrets.token_urlsafe(32)


settings = Settings()
