from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name_surname = StringField('Имя и фамилия пользователя', validators=[DataRequired()])
    nickname = StringField('Ник пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class CharForm(FlaskForm):
    name = StringField('Твоё имя и фамилия:', validators=[DataRequired()])
    about = TextAreaField("О твоём характере:")
    submit = SubmitField('Поделиться')
