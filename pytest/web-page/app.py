from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)





@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/search')
def researcher():
    print(url_for('static', filename='styles.css'))
    return render_template('index.html')
