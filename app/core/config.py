from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DATABASE_URL: str
    UPLOAD_DIR: str
    APP_NAME: str
    APP_VERSION: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()

UPLOAD_DIR = BASE_DIR / settings.UPLOAD_DIR
DATABASE_URL = settings.DATABASE_URL