import graphene

from app.models import User as UserModel, get_session

from .types import User
from .validators import UserCreateValidator


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True, description="The user name")
        email = graphene.String(required=True, description="The user e-mail")

    Output = User

    def mutate(root, info, name: str, email: str) -> UserModel:
        UserCreateValidator(name=name, email=email)

        user = UserModel(name=name, email=email)

        with get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)

        return user
