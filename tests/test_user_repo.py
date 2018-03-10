import pytest
from sqlalchemy.orm import sessionmaker

from models import engine, UserModel
from repositories import UserRepository

from factories import UserFactory
from repositories import ez_sha

Session = sessionmaker()


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()

    yield connection

    connection.close()


@pytest.fixture(scope='function')
def session(connection):
    # begin a non-ORM transaction and bind session
    transaction = connection.begin()
    session = Session(bind=connection)

    UserFactory._meta.sqlalchemy_session = session

    yield session

    # close session and rollback transaction
    session.close()
    transaction.rollback()


@pytest.fixture
def repo(session):
    return UserRepository(session)


def test_authentication_success(repo):
    password = 'user plain password'
    user = UserFactory.create(password=ez_sha(password))

    result = repo.authenticate(user.email, password)

    assert user.id == result.id
    assert user.email == result.email


def test_authentication_fails(repo):
    password = 'user plain password'
    user = UserFactory.create(password=ez_sha(password))

    result = repo.authenticate(user.email, 'yeah i forgot the password')

    assert not result


def test_change_name(session, repo):
    count = 6
    users = UserFactory.create_batch(count)
    chosen_one = users.pop()
    new_first_name = 'Geeno'
    new_last_name = 'Paoly'

    user = repo.change_name(chosen_one.id, new_first_name, new_last_name)

    assert chosen_one.first_name != user.first_name
    assert chosen_one.last_name != user.last_name
    retrieved = session.query(UserModel).get(chosen_one.id)
    assert new_first_name == retrieved.first_name
    assert new_last_name == retrieved.last_name
    assert count == session.query(UserModel).count()


def test_change_name_fails_if_not_existent_user(repo):
    UserFactory.create_batch(6)

    with pytest.raises(Exception):
        repo.change_name('42', 'Foo', 'Bar')
