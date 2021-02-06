import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl

import os


class Settings(BaseSettings):
    PROJECT_NAME: str = 'fastapi vue blog'
    BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    LOG_PATH = os.path.join(BASEDIR, 'logs')

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List = ['*']

    SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{BASEDIR}/fastapi-vue-blog.db'

    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    FIRST_ADMIN = 'admin'
    FIRST_ADMIN_PASSWORD = 'admin'
    NORMAL_TEST_USER = 'demo'
    NORMAL_TEST_USER_PASSWORD = 'demo'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'standard': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'logfile': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASEDIR, 'logs', 'debug.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'db_logfile': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'db.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'run': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'run.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'error': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'error.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
            'test': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_PATH, 'test.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 7,
                'formatter': 'standard'
            },
        },
        'loggers': {
            'fastapi': {
                'handlers': ['run'],
                'level': 'DEBUG',
                'propagate': False
            },
            'uvicorn.access': {
                'handlers': ['run'],
                'level': 'INFO',
                'propagate': False
            },
            'uvicorn.error': {
                'handlers': ['error'],
                'level': 'INFO',
                'propagate': False
            },
            'test': {
                'handlers': ['logfile'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'database': {
                'handlers': ['db_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }


settings = Settings()

if not os.path.exists(settings.LOG_PATH):
    os.makedirs(settings.LOG_PATH)

