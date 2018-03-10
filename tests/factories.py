from datetime import datetime, timezone
from uuid import uuid4

import factory

from models import UserModel
from repositories import ez_sha


def random_sha():
    return ez_sha(str(uuid4()))


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: '%s' % n)
    created = factory.LazyFunction(lambda: datetime.now(tz=timezone.utc))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.LazyFunction(random_sha)

    class Meta:
        model = UserModel
        sqlalchemy_session_persistence = 'commit'
