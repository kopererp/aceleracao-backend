from tests.factories import UserFactory


def test_should_delete_the_user(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            deleteUser(userId: "{user_id}") {{
                success
            }}
        }}
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {"deleteUser": {"success": True}}


def test_should_return_an_error_when_the_user_does_not_exists(client):
    query = """
        mutation {
            deleteUser(userId: "8631d2f7-8ecf-4102-a3e3-42c244a82300") {
                success
            }
        }
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "not found",
            "locations": [{"line": 3, "column": 13}],
            "path": ["deleteUser"],
        }
    ]
