from app.tests.factories import UserFactory


def test_should_return_the_users(session, client):
    UserFactory.create_batch(3)

    query = """
        query {
            users {
                edges {
                    node {
                        userId
                        name
                        email
                    }
                }

            }
        }
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {
        "users": {
            "edges": [
                {
                    "node": {
                        "userId": "8631d2f7-8ecf-4102-a3e3-42c244a82300",
                        "name": "Name 0",
                        "email": "name+0@user.com",
                    }
                },
                {
                    "node": {
                        "userId": "8631d2f7-8ecf-4102-a3e3-42c244a82301",
                        "name": "Name 1",
                        "email": "name+1@user.com",
                    }
                },
                {
                    "node": {
                        "userId": "8631d2f7-8ecf-4102-a3e3-42c244a82302",
                        "name": "Name 2",
                        "email": "name+2@user.com",
                    }
                },
            ]
        }
    }


def test_should_return_an_empty_response_when_there_is_not_users(session, client):
    query = """
        query {
            users {
                edges {
                    node {
                        userId
                        name
                        email
                    }
                }

            }
        }
    """
    response = client.execute(query)
    data = response["data"]

    assert data == {"users": {"edges": []}}
