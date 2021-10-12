import uuid
from unittest.mock import patch


@patch("uuid.uuid4", return_value=uuid.UUID("5a9ee8c5-ed55-4239-9758-5422292dafd0"))
def test_should_create_an_user(uuid_mock, client, set_scoped_session):
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
