from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/pers/<string:name>')
def pers(name):
    return render_template('person.html', mane=name)


@app.route('/')
def index():
    return render_template('base.html', title='9Н')


def main():
    db_session.global_init("db/ninthN.db")
    app.run()


if __name__ == '__main__':
    main()
