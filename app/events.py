from mongoengine import connect, disconnect

from app.settings import settings


def on_application_startup():
    connect(host=settings.MONGO_URI)


def on_application_shutdown():
    disconnect()
