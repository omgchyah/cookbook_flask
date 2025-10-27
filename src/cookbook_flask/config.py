import os
from dotenv import load_dotenv

load_dotenv() # read .env into process environment once

"""
.env + env vars: keep secrets and machine-specific settings out of code.
Config class: single source of truth for the app settings.
"""

"""
DATABASE_URL lets you paste a ready URI (handy for Docker/Prod).
"""

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    
    DATABASE_URL = os.getenv("DATABASE_URL") # full URI optional
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "cookbook_flask")
    
    SQLALCHEMY_DATABASE_URI = (
        DATABASE_URL
        or f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DEBUG = os.getenv("FLASK_DEBUG", "1") == 1
    TESTING = False