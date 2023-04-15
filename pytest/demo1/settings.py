from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    URL_JSPLACEHOLDER: str = Field(..., env='URL_JSPLACEHOLDER')

base_settings = Settings()