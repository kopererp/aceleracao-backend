from app.tests.factories import TwitterMessageFactory


def test_should_delete_the_twitter_message(client):
    twitter_message = TwitterMessageFactory()

    mutation = f"""
        mutation {{
            deleteTwitterMessage(messageId: "{twitter_message.message_id}") {{
                success
            }}
        }}
    """
    response = client.execute(mutation)
    data = response["data"]

    assert data == {"deleteTwitterMessage": {"success": True}}


def test_should_return_not_found_when_there_is_no_twitter_message(client):
    mutation = """
        mutation {
            deleteTwitterMessage(messageId: "5a9ee8c5-ed55-4239-9758-5422292dafd0") {
                success
            }
        }
    """
    response = client.execute(mutation)
    errors = response["errors"]

    assert errors == [
        {
            "message": "not found",
            "locations": [{"line": 3, "column": 13}],
            "path": ["deleteTwitterMessage"],
        }
    ]
