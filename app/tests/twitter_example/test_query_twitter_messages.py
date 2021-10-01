import uuid
from unittest.mock import patch
from app.tests.factories import TwitterMessageFactory


@patch(
    "uuid.uuid4",
    side_effect=[
        uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"),
        uuid.UUID("40fb687d-e30d-46fe-9bf5-a7aad88b3ce0"),
        uuid.UUID("4122df4e-0187-4ab7-aaf5-3b843874ef88"),
        uuid.UUID("c1177d0b-ef72-4624-9598-c1c3c658ef18"),
    ],
)
def test_should_return_the_twitter_messages(uuid_mock, client):
    TwitterMessageFactory.create_batch(3)

    query = """
        query {
            twitterMessages {
                edges {
                    node {
                        messageId
                        createdAt
                        updatedAt
                        title
                        message
                    }
                }

            }
        }
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "twitterMessages": {
            "edges": [
                {
                    "node": {
                        "messageId": "5a9ee8c5-ed55-4239-9758-5422292dafd0",
                        "createdAt": "2021-04-03T00:00:00",
                        "updatedAt": "2021-04-03T00:00:00",
                        "title": "Title 0",
                        "message": "Lorem Lorem 0",
                    }
                },
                {
                    "node": {
                        "messageId": "4122df4e-0187-4ab7-aaf5-3b843874ef88",
                        "createdAt": "2021-04-04T00:00:00",
                        "updatedAt": "2021-04-04T00:00:00",
                        "title": "Title 1",
                        "message": "Lorem Lorem 1",
                    }
                },
                {
                    "node": {
                        "messageId": "c1177d0b-ef72-4624-9598-c1c3c658ef18",
                        "createdAt": "2021-04-05T00:00:00",
                        "updatedAt": "2021-04-05T00:00:00",
                        "title": "Title 2",
                        "message": "Lorem Lorem 2",
                    }
                },
            ]
        }
    }


def test_should_return_empty_when_there_is_not_twitter_messages(client):
    query = """
        query {
            twitterMessages {
                edges {
                    node {
                        messageId
                        createdAt
                        updatedAt
                        title
                        message
                    }
                }

            }
        }
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {"twitterMessages": {"edges": []}}
