from mongoengine import connect, disconnect

from app.models import Base, engine
from app.settings import settings


def on_application_startup():
    connect(host=settings.MONGO_URI)
    Base.metadata.create_all(engine)


def on_application_shutdown():
    disconnect()
