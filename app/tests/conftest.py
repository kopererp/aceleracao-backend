import pendulum
import pytest
from app.main import schema
from app.settings import settings
from graphene.test import Client
from mongoengine import connect, disconnect

from .factories import TwitterMessageFactory


@pytest.fixture(scope="function", autouse=True)
def create_mongo_connection(request):
    host = settings.MONGO_URI.replace("dio", "")
    database = connect("test", host=host)

    def finalizer():
        database.drop_database("test")
        disconnect()

    request.addfinalizer(finalizer)


@pytest.fixture(autouse=True)
def frezee_time():
    now = pendulum.datetime(2021, 4, 3)
    pendulum.set_test_now(now)

    yield

    pendulum.set_test_now()


@pytest.fixture(autouse=True)
def reset_factories_sequences():
    TwitterMessageFactory.reset_sequence(0)


@pytest.fixture
def client():
    yield Client(schema)
