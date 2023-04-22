# импорт необходимых библиотек
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired


# создание полей для ввода информации для регистрации
class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name_surname = StringField('Имя и фамилия пользователя', validators=[DataRequired()])
    nickname = StringField('Ник пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')


# создание полей для ввода информации для авторизации
class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


# создание поля для ввода информации об авторизованном однокласснике
class CharForm(FlaskForm):
    about = TextAreaField("О твоём характере:")
    submit = SubmitField('Поделиться')
