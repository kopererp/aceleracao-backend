import graphene

from .twitter_example.mutations import TwitterMessageMutation
from .twitter_example.queries import TwitterMessageQuery


class Query(TwitterMessageQuery):
    pass


class Mutation(graphene.ObjectType):
    create_twitter_message = TwitterMessageMutation.Field()
