import os
from dotenv import load_dotenv

load_dotenv() # read .env into process environment once

"""
.env + env vars: keep secrets and machine-specific settings out of code.
Config class: single source of truth for the app settings.
"""

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    DEBUG = os.getenv("FLASK_DEBUG", "1") == 1
    TESTING = False