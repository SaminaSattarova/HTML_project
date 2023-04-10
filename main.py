from flask import Flask, render_template
from data import db_session
from data.mates import Classmates

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    mates = {}
    for elem in db_sess.query(Classmates):
        mates[elem.name] = [elem.about, elem.travels]
    return render_template('base.html', title='9Н', people=mates)



def main():
    db_session.global_init("db/ninthN.db")
    app.run()


if __name__ == '__main__':
    main()
