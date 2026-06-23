from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    PORT: int = 8000
    ENV: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()