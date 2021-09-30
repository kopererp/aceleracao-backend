from os import path

import pydantic
from fastapi.templating import Jinja2Templates


class Settings(pydantic.BaseSettings):
    MONGO_URI: pydantic.AnyUrl = "mongodb://mongo/dio"
    POSTGRES_URI: pydantic.PostgresDsn = "postgresql://dio:dio@postgres:5432"

    BASE_DIR = path.abspath(path.dirname(__file__))
    TEMPLATE_DIR = path.join(BASE_DIR, "templates")

    class Config:
        env_file = path.join(path.dirname(__file__), ".env")


settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
