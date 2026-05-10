# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./agri_mgmt.db"
    # Add more config as needed

settings = Settings()
