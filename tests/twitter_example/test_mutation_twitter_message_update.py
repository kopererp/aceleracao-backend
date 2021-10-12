import uuid
from unittest.mock import patch

from tests.factories import TwitterMessageFactory


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_update_the_twitter_message_title(uuid_mock, client):
    twitter_message = TwitterMessageFactory(title="Title", message="Lore Lorem")

    mutation = f"""
        mutation {{
            updateTwitterMessage(messageId: "{twitter_message.message_id}", title: "New Title") {{
                messageId
                createdAt
                updatedAt
                title
                message
            }}
        }}
    """
    response = client.execute(mutation)
    data = response["data"]

    assert data == {
        "updateTwitterMessage": {
            "messageId": "5a9ee8c5-ed55-4239-9758-5422292dafd0",
            "createdAt": "2021-04-03T00:00:00",
            "updatedAt": "2021-04-03T00:00:00",
            "title": "New Title",
            "message": "Lore Lorem",
        }
    }


def test_should_check_the_title_max_length(client):
    twitter_message = TwitterMessageFactory(title="Title", message="Lore Lorem")
    new_title = "T" * 82

    mutation = f"""
        mutation {{
            updateTwitterMessage(messageId: "{twitter_message.message_id}", title: "{new_title}") {{
                messageId
                createdAt
                updatedAt
                title
                message
            }}
        }}
    """
    response = client.execute(mutation)
    errors = response["errors"]

    assert errors == [
        {
            "message": "ensure this value has at most 80 characters",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateTwitterMessage"],
        }
    ]


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_update_the_twitter_message_message(uuid_mock, client):
    twitter_message = TwitterMessageFactory(title="Title", message="Lore Lorem")

    mutation = f"""
        mutation {{
            updateTwitterMessage(messageId: "{twitter_message.message_id}", message: "Merol merol") {{
                messageId
                createdAt
                updatedAt
                title
                message
            }}
        }}
    """
    response = client.execute(mutation)
    data = response["data"]

    assert data == {
        "updateTwitterMessage": {
            "messageId": "5a9ee8c5-ed55-4239-9758-5422292dafd0",
            "createdAt": "2021-04-03T00:00:00",
            "updatedAt": "2021-04-03T00:00:00",
            "title": "Title",
            "message": "Merol merol",
        }
    }


def test_should_check_the_message_max_length(client):
    twitter_message = TwitterMessageFactory(title="Title", message="Lore Lorem")
    new_message = "T" * 281

    mutation = f"""
        mutation {{
            updateTwitterMessage(messageId: "{twitter_message.message_id}", message: "{new_message}") {{
                messageId
                createdAt
                updatedAt
                title
                message
            }}
        }}
    """
    response = client.execute(mutation)
    errors = response["errors"]

    assert errors == [
        {
            "message": "ensure this value has at most 280 characters",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateTwitterMessage"],
        }
    ]


def test_should_return_not_found_when_there_is_no_twitter_message(client):
    mutation = """
        mutation {
            updateTwitterMessage(messageId: "5a9ee8c5-ed55-4239-9758-5422292dafd0") {
                messageId
                createdAt
                updatedAt
                title
                message
            }
        }
    """
    response = client.execute(mutation)
    errors = response["errors"]

    assert errors == [
        {
            "message": "not found",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateTwitterMessage"],
        }
    ]
