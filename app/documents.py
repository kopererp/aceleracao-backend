import uuid

import pendulum
from mongoengine import DateTimeField, Document, StringField, UUIDField


def generate_id():
    return uuid.uuid4()


class TwitterMessage(Document):
    message_id = UUIDField(
        primary_key=True,
        db_field="messageId",
        default=generate_id,
        help_text="Identification of the message",
    )
    created_at = DateTimeField(db_field="createdAt", default=pendulum.now, help_text="Date of creation")
    updated_at = DateTimeField(db_field="updateAt", default=pendulum.now, help_text="Date of the last update")
    title = StringField(help_text="Title of the message")
    message = StringField(help_text="The description of the message")
