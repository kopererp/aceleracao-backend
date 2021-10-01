import uuid
from unittest.mock import patch

from app.tests.factories import TwitterMessageFactory


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_create_the_twitter_message(uuid_mock, client):
    mutation = """
        mutation {
            createTwitterMessage(title: "Title", message: "Lorem lorem") {
                messageId
                createdAt
                updatedAt
                title
                message
            }
        }
    """
    response = client.execute(mutation)
    data = response["data"]

    assert data == {
        "createTwitterMessage": {
            "messageId": "5a9ee8c5-ed55-4239-9758-5422292dafd0",
            "createdAt": "2021-04-03T00:00:00+00:00",
            "updatedAt": "2021-04-03T00:00:00+00:00",
            "title": "Title",
            "message": "Lorem lorem",
        }
    }


def test_should_check_the_title_max_length(client):
    new_title = "T" * 82

    mutation = f"""
        mutation {{
            createTwitterMessage(title: "{new_title}", message: "Lorem lorem") {{
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
            "path": ["createTwitterMessage"],
        }
    ]


def test_should_check_the_title_required(client):
    new_title = "T" * 82

    mutation = f"""
        mutation {{
            createTwitterMessage(message: "Lorem lorem") {{
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
            "message": 'Field "createTwitterMessage" argument "title" of type "String!" is required but not provided.',
            "locations": [{"line": 3, "column": 13}],
        }
    ]


def test_should_check_the_message_max_length(client):
    message = "T" * 281

    mutation = f"""
        mutation {{
            createTwitterMessage(title: "Title", message: "{message}") {{
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
            "path": ["createTwitterMessage"],
        }
    ]


def test_should_check_the_title_required(client):

    mutation = f"""
        mutation {{
            createTwitterMessage(title: "Title") {{
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
            "message": 'Field "createTwitterMessage" argument "message" of type "String!" is required but not provided.',
            "locations": [{"line": 3, "column": 13}],
        }
    ]