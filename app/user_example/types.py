from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
