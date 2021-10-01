import pendulum
import pytest
from graphene.test import Client
from mongoengine import connect, disconnect
from sqlalchemy.schema import CreateSchema, DropSchema

from app.main import schema
from app.models import Base, ScopedSession, engine
from app.settings import settings

from .factories import TwitterMessageFactory, UserFactory


@pytest.fixture(scope="function", autouse=True)
def create_mongo_connection(request):
    host = settings.MONGO_URI.replace("dio", "")
    database = connect("test", host=host)

    def finalizer():
        database.drop_database("test")
        disconnect()

    request.addfinalizer(finalizer)


@pytest.fixture(scope="session", autouse=True)
def create_schema(request):
    if not engine.dialect.has_schema(engine, "test"):
        engine.execute(CreateSchema("test"))
    else:
        engine.execute(DropSchema("test", cascade=True))

    connection = engine.connect()
    connection.execute(f"SET search_path to 'test'")
    connection.dialect.default_schema_name = "test"
    Base.metadata.create_all(connection)

    def drop_schema():
        Base.metadata.drop_all(connection)
        engine.execute(DropSchema("test", cascade=True))
        engine.dispose()

    request.addfinalizer(drop_schema)


@pytest.fixture(scope="function", autouse=True)
def truncate_tables():
    connection = engine.connect()
    transaction = connection.begin()

    tables = ",".join(f'"test".{table.name}' for table in reversed(Base.metadata.sorted_tables))
    connection.execute(f"TRUNCATE {tables} RESTART IDENTITY;")
    transaction.commit()


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


@pytest.fixture
def session():
    scoped_session = ScopedSession()
    scoped_session.connection(execution_options={"schema_translate_map": {None: "test"}})

    try:
        yield scoped_session
    finally:
        scoped_session.rollback()
        ScopedSession.remove()