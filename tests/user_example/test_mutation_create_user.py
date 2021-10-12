import uuid
from unittest.mock import patch


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_create_an_user(uuid_mock, client):
    query = """
        mutation {
            createUser(name: "User", email: "user@user.com") {
                userId
                name
                email
            }
        }
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "createUser": {"userId": "5a9ee8c5-ed55-4239-9758-5422292dafd0", "name": "User", "email": "user@user.com"}
    }


def test_should_return_an_error_on_empty_name(client):
    query = """
        mutation {
            createUser(name: "", email: "user@user.com") {
                userId
                name
                email
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "ensure this value has at least 1 characters",
            "locations": [{"line": 3, "column": 13}],
            "path": ["createUser"],
        }
    ]


def test_should_return_an_error_on_invalid_email(client):
    query = """
        mutation {
            createUser(name: "User", email: "invalid@email") {
                userId
                name
                email
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "value is not a valid email address",
            "locations": [{"line": 3, "column": 13}],
            "path": ["createUser"],
        }
    ]


def test_should_return_an_error_on_empty_email(client):
    query = """
        mutation {
            createUser(name: "User", email: "") {
                userId
                name
                email
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "value is not a valid email address",
            "locations": [{"line": 3, "column": 13}],
            "path": ["createUser"],
        }
    ]