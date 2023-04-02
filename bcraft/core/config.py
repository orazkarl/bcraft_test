from typing import Optional, List, Union, Dict, Any

from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl, validator
from pydantic.env_settings import DotenvType


class Settings(BaseSettings):
    PROJECT_NAME: str = 'BCRAFT TEST'
    DEBUG = False
    API_V1_STR: str = "/api"
    SERVER_NAME: str = 'bcraft'
    SERVER_HOST: AnyHttpUrl = 'http://localhost'

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file: Optional[DotenvType] = "./.env"


settings = Settings()
