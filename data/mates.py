import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Classmates(SqlAlchemyBase):
    __tablename__ = 'mates'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    travels = sqlalchemy.Column(sqlalchemy.String, nullable=True)
