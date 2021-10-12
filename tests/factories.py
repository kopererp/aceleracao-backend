import factory
import pendulum
from app.documents import TwitterMessage
from app.models import User, ScopedSession


class TwitterMessageFactory(factory.mongoengine.MongoEngineFactory):
    created_at = factory.Sequence(lambda n: pendulum.now().add(days=n))
    updated_at = factory.Sequence(lambda n: pendulum.now().add(days=n))
    title = factory.Sequence(lambda n: f"Title {n}")
    message = factory.Sequence(lambda n: f"Lorem Lorem {n}")

    class Meta:
        model = TwitterMessage


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    user_id = factory.Sequence(lambda n: f"8631d2f7-8ecf-4102-a3e3-42c244a823{n:0>2}")
    name = factory.Sequence(lambda n: f"Name {n}")
    email = factory.Sequence(lambda n: f"name+{n}@user.com")

    class Meta:
        model = User
        sqlalchemy_session = ScopedSession
