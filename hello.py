from flask import Flask, redirect, abort
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    user = name
    if name=="sun":
        abort(404)
    return '<h1>Hello, %s!' % name

@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')

if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()


