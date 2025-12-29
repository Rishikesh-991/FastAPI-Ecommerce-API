from pydantic_settings import BaseSettings
# add jenkins file in that

class Settings(BaseSettings):
    # Database  the Config
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str

    # JWT the changes Config
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
