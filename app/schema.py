import graphene
from graphene.relay import Node

from .twitter_example.mutations import (
    TwitterMessageCreateMutation,
    TwitterMessageDeleteMutation,
    TwitterMessageUpdateMutation,
)
from .twitter_example.queries import TwitterMessageQuery
from .user_example.queries import UserQuery
from .user_example.mutations import UserCreateMutation


class Query(TwitterMessageQuery, UserQuery):
    node = Node.Field()


class Mutation(graphene.ObjectType):
    create_twitter_message = TwitterMessageCreateMutation.Field()
    update_twitter_message = TwitterMessageUpdateMutation.Field()
    delete_twitter_message = TwitterMessageDeleteMutation.Field()

    create_user = UserCreateMutation.Field()
