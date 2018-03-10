from hashlib import sha256

from models import UserModel


def ez_sha(s, encoding='UTF-8'):
    return sha256(s.encode(encoding)).hexdigest()


class UserRepository:
    model_cls = UserModel

    def __init__(self, session):
        self.session = session

    def authenticate(self, email, password):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.email == email)
        query = query.filter(self.model_cls.password == ez_sha(password))

        return query.one_or_none()

    def change_name(self, user_id, first_name, last_name):
        query = self.session.query(self.model_cls)
        query = query.filter(self.model_cls.id == user_id)
        query = query.with_for_update()
        user = query.one()

        user.first_name = first_name
        user.last_name = last_name

        self.session.flush()

        return user
