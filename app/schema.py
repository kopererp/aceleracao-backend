import graphene

from .twitter_example.mutations import (
    TwitterMessageCreateMutation,
    TwitterMessageUpdateMutation,
)
from .twitter_example.queries import TwitterMessageQuery


class Query(TwitterMessageQuery):
    pass


class Mutation(graphene.ObjectType):
    create_twitter_message = TwitterMessageCreateMutation.Field()
    update_twitter_message = TwitterMessageUpdateMutation.Field()
