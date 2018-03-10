import os

from sqlalchemy import (
    BigInteger,
    create_engine,
    Column,
    DateTime,
    String,
    text
)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ['DB_URL'])
Base = declarative_base(bind=engine)


class UserModel(Base):
    __tablename__ = 'account'

    id = Column(BigInteger, primary_key=True)
    created = Column(DateTime(timezone=True), server_default=text('now()'))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
