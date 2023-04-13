from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data import db_session
from data.mates import Classmates
from data.users import User
from data.news import News
from forms.user import RegisterForm, LoginForm
import subprocess
cmd = 'python tg_bot.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    mates = {}
    for elem in db_sess.query(Classmates):
        mates[elem.name] = [elem.character, elem.hobby, elem.travels]
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    if current_user.is_authenticated:
        if current_user.is_classmate:
            return render_template('base.html', title='9Н', people=mates, classmate=True, name=current_user.name)
    return render_template('base.html', title='9Н', people=mates, classmate=False, name='')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        if db_sess.query(Classmates).filter(Classmates.name == form.name_surname.data).first():
            user = User(
               name=form.name_surname.data,
               email=form.email.data,
               nickname=form.nickname.data,
               is_classmate=1
            )
        else:
            user = User(
                name=form.name_surname.data,
                email=form.email.data,
                nickname=form.nickname.data,
                is_classmate=0
            )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/ninthN.db")
    app.run()


if __name__ == '__main__':
    main()
