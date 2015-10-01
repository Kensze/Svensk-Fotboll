from bottle import route, run, template
import json

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def returnsingle():
        return { "id": 1, "name": "Test Item 1" }

run(host='localhost', port=8080, debug=True, reloader=True)
