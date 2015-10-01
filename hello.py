from bottle import route, run, template

@route('/')
def index():
    return template("index")

run(host='localhost', port=8080, debug=True, reloader=True)
