# импорт необходимых библиотек
import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


# создание полей с информацией о поездках в бд
class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    moments = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    conclusion = sqlalchemy.Column(sqlalchemy.String, nullable=True)
