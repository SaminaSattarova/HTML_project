# импорт необходимых библиотек
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


# создание полей с информацией про одноклассников в базе данных
class Classmate(SqlAlchemyBase):
    __tablename__ = 'mates'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    character = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hobby = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    travels = sqlalchemy.Column(sqlalchemy.String, nullable=True)
