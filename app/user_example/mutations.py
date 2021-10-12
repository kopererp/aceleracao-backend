from typing import Optional
from uuid import UUID

import graphene
from pydantic import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from app.models import User as UserModel, get_session

from .types import User
from .validators import UserCreateValidator, UserUpdateValidator


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True, description="The user name")
        email = graphene.String(required=True, description="The user e-mail")

    Output = User

    def mutate(root, info, name: str, email: str) -> UserModel:
        try:
            UserCreateValidator(name=name, email=email)

            user = UserModel(name=name, email=email)

            with get_session() as session:
                session.add(user)
                session.commit()
                session.refresh(user)

            return user

        except ValidationError as e:
            error = e.errors()[0]["msg"]
            raise Exception(error)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True, description="The user identification")
        name = graphene.String(required=False, description="The user name")
        email = graphene.String(required=False, description="The user e-mail")

    Output = User

    def mutate(root, info, user_id: UUID, **kwargs) -> UserModel:
        try:
            UserUpdateValidator(**kwargs)

            with get_session() as session:
                user = UserModel.query.filter_by(user_id=user_id).one()

                for key, value in kwargs.items():
                    if not value:
                        continue

                    setattr(user, key, value)

                session.add(user)
                session.commit()
                session.refresh(user)

            return user

        except NoResultFound:
            raise Exception("not found")

        except ValidationError as e:
            error = e.errors()[0]["msg"]
            raise Exception(error)
