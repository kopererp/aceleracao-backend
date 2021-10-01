import factory
import pendulum
from app.documents import TwitterMessage


class TwitterMessageFactory(factory.mongoengine.MongoEngineFactory):
    created_at = factory.Sequence(lambda n: pendulum.now().add(days=n))
    updated_at = factory.Sequence(lambda n: pendulum.now().add(days=n))
    title = factory.Sequence(lambda n: f"Title {n}")
    message = factory.Sequence(lambda n: f"Lorem Lorem {n}")

    class Meta:
        model = TwitterMessage
