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


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": None}

    user_id = sa.Column(UUID(as_uuid=True), primary_key=True)
    name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
