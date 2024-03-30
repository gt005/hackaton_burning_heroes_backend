import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Main database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str

    # Auth settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_LIFETIME: int
    REFRESH_TOKEN_LIFETIME: int

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}" \
               f"@{self.DB_HOST}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env" if os.path.isfile(".env") else ".env.example"


settings = Settings()
