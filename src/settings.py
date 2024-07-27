from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Union

class Settings(BaseSettings):
    openai_api_key: str = Field(validation_default="OPENAI_API_KEY")
    openai_model: str = Field(validation_default="OPENAI_MODEL")

    model_config = SettingsConfigDict(env_file=".env")

settings: Union[Settings | None] = None

def get_settings():
    global settings

    if settings is None:
        settings = Settings()
    
    return settings