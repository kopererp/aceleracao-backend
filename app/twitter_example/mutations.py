import graphene

from app.documents import TwitterMessage as TwitterMessageDocument
from .types import TwitterMessage


class TwitterMessageMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(description="Title of the message")
        message = graphene.String(description="Description of the message")

    Output = TwitterMessage

    def mutate(self, info, title: str, message: str) -> TwitterMessageDocument:
        twitter_message = TwitterMessageDocument(title=title, message=message)
        twitter_message.save()

        return twitter_message