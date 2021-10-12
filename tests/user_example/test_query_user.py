from tests.factories import UserFactory


def test_should_return_the_user(client):
    user = UserFactory()

    query = f"""
        query {{
            user(userId: "{user.user_id}") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "user": {"userId": "8631d2f7-8ecf-4102-a3e3-42c244a82300", "name": "Name 0", "email": "name+0@user.com"}
    }


def test_should_return_an_error_when_there_is_not_user(client):
    query = """
        query {
            user(userId: "8631d2f7-8ecf-4102-a3e3-42c244a82300") {
                userId
                name
                email
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [{"message": "not found", "locations": [{"line": 3, "column": 13}], "path": ["user"]}]
