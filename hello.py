from bottle import route, run, template
import json

@route('/')
def index():
    return template("index")

<<<<<<< HEAD
=======
@route('/')
def returnsingle():
        return { "id": 1, "name": "Test Item 1" }

>>>>>>> origin/master
run(host='localhost', port=8080, debug=True, reloader=True)
