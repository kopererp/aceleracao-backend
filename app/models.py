import uuid
from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.settings import settings

engine = create_engine(settings.POSTGRES_URI)
Session = sessionmaker(autocommit=False, bind=engine)
ScopedSession = scoped_session(Session)

Base = declarative_base()
Base.query = ScopedSession.query_property()


@contextmanager
def get_session():
    session = ScopedSession()

    try:
        yield session
    finally:
        ScopedSession.remove()


def generate_id() -> uuid.UUID:
    return uuid.uuid4()


class User(Base):
    __tablename__ = "user"

    user_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=generate_id)
    name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
