# импорт необходимых библиотек
import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# создание полей с информацией о пользователях в бд
class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_classmate = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    # добавление в бд захэшированного пароля
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # проверка пароля при авторизации, регистрации и повторном вводе
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)