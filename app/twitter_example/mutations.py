from uuid import UUID

import graphene
from pydantic import ValidationError

from app.documents import TwitterMessage as TwitterMessageDocument

from .types import SuccessDelete, TwitterMessage
from .validators import TwitterMessageCreateValidator, TwitterMessageUpdateValidator


class TwitterMessageCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True, description="Title of the message")
        message = graphene.String(required=True, description="Description of the message")

    Output = TwitterMessage

    def mutate(self, info, title: str, message: str) -> TwitterMessageDocument:
        try:
            TwitterMessageCreateValidator(title=title, message=message)
            twitter_message = TwitterMessageDocument(title=title, message=message)
            twitter_message.save()

            return twitter_message
        except ValidationError as e:
            error = e.errors()[0]["msg"]
            raise Exception(error)


class TwitterMessageUpdateMutation(graphene.Mutation):
    class Arguments:
        message_id = graphene.ID(required=True, description="Identification of the message")
        title = graphene.String(required=False, description="Title of the message")
        message = graphene.String(required=False, description="Description of the message")

    Output = TwitterMessage

    def mutate(self, info, message_id: UUID, **kwargs) -> TwitterMessageDocument:
        try:
            TwitterMessageUpdateValidator(**kwargs)
            twitter_message = TwitterMessageDocument.objects.get(message_id=message_id)

            for key, value in kwargs.items():
                if not value:
                    continue

                setattr(twitter_message, key, value)

            twitter_message.save()
            return twitter_message
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")

        except ValidationError as e:
            error = e.errors()[0]["msg"]
            raise Exception(error)


class TwitterMessageDeleteMutation(graphene.Mutation):
    class Arguments:
        message_id = graphene.ID(required=True, description="Identification of the message")

    Output = SuccessDelete

    def mutate(self, info, message_id: UUID) -> SuccessDelete:
        try:
            twitter_message = TwitterMessageDocument.objects.get(message_id=message_id)
            twitter_message.delete()

            return SuccessDelete(success=True)
        except TwitterMessageDocument.DoesNotExist:
            raise Exception("not found")
