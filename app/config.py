from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_user: str
    mysql_password: str
    mysql_database: str
    mysql_host: str
    mysql_port: int = 3306

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()