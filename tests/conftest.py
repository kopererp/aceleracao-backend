import pendulum
import pytest
from graphene.test import Client
from mongoengine import connect, disconnect
from sqlalchemy import create_engine

from app import models
from app.main import schema
from app.settings import settings

from .factories import TwitterMessageFactory, UserFactory

test_engine = create_engine(f"{settings.POSTGRES_URI}/test")


@pytest.fixture(scope="function")
def config():
    settings.POSTGRES_URI = f"{settings.POSTGRES_URI}/test"


@pytest.fixture(autouse=True)
def set_scoped_session():
    models.ScopedSession.configure(bind=test_engine)


@pytest.fixture(scope="function", autouse=True)
def create_mongo_connection(request):
    host = settings.MONGO_URI.replace("dio", "")
    database = connect("test", host=host)

    def finalizer():
        database.drop_database("test")
        disconnect()

    request.addfinalizer(finalizer)


@pytest.fixture(scope="session", autouse=True)
def create_database(request):
    engine = create_engine(settings.POSTGRES_URI)

    with engine.connect() as connection:
        connection.execution_options(isolation_level="AUTOCOMMIT")
        connection.execute("DROP DATABASE IF EXISTS test")
        connection.execute("CREATE DATABASE test")

    models.Base.metadata.bind = test_engine


@pytest.fixture(scope="function", autouse=True)
def clean_database():
    models.Base.metadata.create_all()

    yield

    models.ScopedSession.remove()
    models.Base.metadata.drop_all()


@pytest.fixture(autouse=True)
def frezee_time():
    now = pendulum.datetime(2021, 4, 3)
    pendulum.set_test_now(now)

    yield

    pendulum.set_test_now()


@pytest.fixture(autouse=True)
def reset_factories_sequences():
    TwitterMessageFactory.reset_sequence(0)
    UserFactory.reset_sequence(0)


@pytest.fixture
def client():
    yield Client(schema)
