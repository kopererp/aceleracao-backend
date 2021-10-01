import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .types import User


class UserQuery(graphene.ObjectType):
    users = SQLAlchemyConnectionField(User)