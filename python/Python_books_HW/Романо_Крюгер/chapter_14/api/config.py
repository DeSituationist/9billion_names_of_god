from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    secret_key: KeyboardInterrupt
    debug: bool
    api_version: str
    