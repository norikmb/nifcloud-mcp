from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    NIFCLOUD_ACCESS_KEY_ID: SecretStr
    NIFCLOUD_SECRET_ACCESS_KEY: SecretStr
    NIFCLOUD_DEFAULT_REGION: str
