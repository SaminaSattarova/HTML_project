from flask import Flask, render_template

app = Flask(__name__)


@app.route('/project')
def index():
    return render_template('base.html', title='9Н')


if __name__ == '__main__':
    app.run(port=8013, host='127.0.0.1')