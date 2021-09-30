import graphene
from app.documents import TwitterMessage as TwitterMessageDocument

from .types import TwitterMessage


class TwitterMessageQuery(graphene.ObjectType):
    twitter_message = graphene.Field(
        TwitterMessage,
        id=graphene.ID(required=True, description="Message's identification"),
    )

    def resolve_twitter_message(root, info, id: graphene.ID) -> TwitterMessage:
        try:
            return TwitterMessageDocument.objects.get(message_id=id)
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")
