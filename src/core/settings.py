from pydantic import BaseSettings

class Settings(BaseSettings):
    SERVER_HOST: str = '0.0.0.0'
    SERVER_PORT: int = 8000

    DATABASE_URL: str = ''
    

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
