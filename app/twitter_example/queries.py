from typing import List
from uuid import UUID

import graphene
from app.documents import TwitterMessage as TwitterMessageDocument

from .types import TwitterMessage


class TwitterMessageQuery(graphene.ObjectType):
    twitter_message = graphene.Field(
        TwitterMessage,
        message_id=graphene.ID(required=True, description="Message's identification"),
    )
    twitter_messages = graphene.List(TwitterMessage)

    def resolve_twitter_message(root, info, message_id: UUID) -> TwitterMessageDocument:
        try:
            return TwitterMessageDocument.objects.get(message_id=message_id)
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")

    def resolve_twitter_messages(root, info) -> List[TwitterMessageDocument]:
        return TwitterMessageDocument.objects.all()
