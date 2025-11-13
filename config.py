from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    db_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    postgresql_test_database_uri: str
    postgresql_admin_database_uri: str

    class Config:
        env_file = ".env"

settings = Settings()