from tests.factories import UserFactory


def test_should_update_the_user_name(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            updateUser(userId: "{user_id}", name: "New User Name", email: "new_email@user.com") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "updateUser": {
            "userId": user_id,
            "name": "New User Name",
            "email": "new_email@user.com",
        }
    }


def test_should_update_the_user_email(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            updateUser(userId: "{user_id}", email: "new_email@user.com") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "updateUser": {
            "userId": user_id,
            "name": "Name 0",
            "email": "new_email@user.com",
        }
    }


def test_should_return_an_error_when_the_user_does_not_exists(client):
    query = """
        mutation {
            updateUser(userId: "8631d2f7-8ecf-4102-a3e3-42c244a82300", email: "new_email@user.com") {
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
            "message": "not found",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateUser"],
        }
    ]


def test_should_return_an_error_on_empty_name(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            updateUser(userId: "{user_id}", name: "") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "ensure this value has at least 1 characters",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateUser"],
        }
    ]


def test_should_return_an_error_on_invalid_email(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            updateUser(userId: "{user_id}", email: "new-email@user") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "value is not a valid email address",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateUser"],
        }
    ]


def test_should_return_an_error_on_empty_email(client):
    user = UserFactory()
    user_id = user.user_id

    query = f"""
        mutation {{
            updateUser(userId: "{user_id}", email: "") {{
                userId
                name
                email
            }}
        }}
    """
    response = client.execute(query)
    errors = response["errors"]

    assert errors == [
        {
            "message": "value is not a valid email address",
            "locations": [{"line": 3, "column": 13}],
            "path": ["updateUser"],
        }
    ]