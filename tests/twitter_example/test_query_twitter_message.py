import uuid
from unittest.mock import patch

from tests.factories import TwitterMessageFactory


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_return_the_twitter_message(uuid_mock, client):
    twitter_message = TwitterMessageFactory()

    query = f"""
        query {{
            twitterMessage(messageId: "{twitter_message.message_id}") {{
                messageId
                createdAt
                updatedAt
                title
                message
            }}
        }}
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "twitterMessage": {
            "messageId": "5a9ee8c5-ed55-4239-9758-5422292dafd0",
            "createdAt": "2021-04-03T00:00:00",
            "updatedAt": "2021-04-03T00:00:00",
            "title": "Title 0",
            "message": "Lorem Lorem 0",
        }
    }


def test_should_return_an_error_when_twitter_message_is_not_found(client):
    query = """
        query {
            twitterMessage(messageId: "5a9ee8c5-ed55-4239-9758-5422292dafd0") {
                messageId
                createdAt
                updatedAt
                title
                message
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "not found",
            "locations": [{"line": 3, "column": 13}],
            "path": ["twitterMessage"],
        }
    ]
