from uuid import UUID

import graphene
from sqlalchemy.orm.exc import NoResultFound
from graphene_sqlalchemy import SQLAlchemyConnectionField

from app.models import User as UserModel
from .types import User


class UserQuery(graphene.ObjectType):
    user = graphene.Field(
        User, user_id=graphene.ID(required=True, description="The user identification"), description="Return an user"
    )
    users = SQLAlchemyConnectionField(User, description="Return a list of users")

    def resolve_user(root, info, user_id: UUID):
        try:
            return UserModel.query.filter_by(user_id=user_id).one()
        except NoResultFound:
            raise Exception("not found")