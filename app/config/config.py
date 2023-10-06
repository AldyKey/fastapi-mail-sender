import sys
from typing import Any, Dict, List, Optional
from os import environ
from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8080))

    MAIL_USERNAME: str = environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = environ.get("MAIL_PASSWORD", "")
    MAIL_PORT: str = int(environ.get("MAIL_PORT", ""))
    MAIL_SERVER: str = environ.get("MAIL_SERVER", "")

    MAIL_TEST: str = environ.get("MAIL_TEST", "")

    @property
    def smtp_settings(self):
        return ConnectionConfig(
            MAIL_USERNAME=self.MAIL_USERNAME,
            MAIL_PASSWORD=self.MAIL_PASSWORD,
            MAIL_PORT=self.MAIL_PORT,
            MAIL_SERVER=self.MAIL_SERVER,
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            MAIL_FROM="aldyk0209@gmail.com"
        )


settings = Settings()
