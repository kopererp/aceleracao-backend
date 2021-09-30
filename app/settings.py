import pydantic


class Settings(pydantic.BaseSettings):
    MONGO_URI: pydantic.AnyUrl = "mongodb://mongo/dio"
    POSTGRES_URI: pydantic.PostgresDsn = "postgresql://dio:dio@postgres:5432"

    class Config:
        env_file = ".env"


settings = Settings()
