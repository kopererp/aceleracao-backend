from typing import List
from uuid import UUID

import graphene
from app.documents import TwitterMessage as TwitterMessageDocument
from graphene_mongo import MongoengineConnectionField

from .types import TwitterMessage


class TwitterMessageQuery(graphene.ObjectType):
    twitter_message = graphene.Field(
        TwitterMessage,
        message_id=graphene.ID(required=True, description="Message's identification"),
    )
    twitter_messages = MongoengineConnectionField(TwitterMessage)

    def resolve_twitter_message(root, info, message_id: UUID) -> TwitterMessageDocument:
        try:
            return TwitterMessageDocument.objects.get(message_id=message_id)
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")

    def resolve_twitter_messages(root, info) -> List[TwitterMessageDocument]:
        return TwitterMessageDocument.objects.all()
