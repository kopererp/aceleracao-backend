from typing import Optional
from uuid import UUID

import graphene
from app.documents import TwitterMessage as TwitterMessageDocument

from .types import TwitterMessage


class TwitterMessageCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True, description="Title of the message")
        message = graphene.String(
            required=True, description="Description of the message"
        )

    Output = TwitterMessage

    def mutate(self, info, title: str, message: str) -> TwitterMessageDocument:
        twitter_message = TwitterMessageDocument(title=title, message=message)
        twitter_message.save()

        return twitter_message


class TwitterMessageUpdateMutation(graphene.Mutation):
    class Arguments:
        message_id = graphene.ID(
            required=True, description="Identification of the message"
        )
        title = graphene.String(required=False, description="Title of the message")
        message = graphene.String(
            required=False, description="Description of the message"
        )

    Output = TwitterMessage

    def mutate(self, info, message_id: UUID, **kwargs) -> TwitterMessageDocument:
        try:
            twitter_message = TwitterMessageDocument.objects.get(message_id=message_id)

            for key, value in kwargs.items():
                if not value:
                    continue

                setattr(twitter_message, key, value)

            twitter_message.save()
            return twitter_message
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")
