import urllib2
import urllib
import json
from flask import Flask, render_template, jsonify, request
from flask.ext.triangle import Triangle

app = Flask(__name__, static_path='/static')
Triangle(app)
app.debug = True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/update", methods=['POST', 'GET'])
def search():
        post = request.get_json()
        query = post.get('search')
        parameters = {'s' : query, 'r' : 'json'}
        response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
        movies = json.loads(response.read())
        return jsonify(movies)


@app.route('/trailer', methods=['POST', 'GET'])
def trailer():

        post = request.get_json()
        query = post.get('search')
        parameters = {'movie' : query, 'limit' : 5, 'width' : 320}
        tmp = 'http://trailersapi.com/trailers.json?' + urllib.urlencode(parameters)
        response = urllib2.urlopen('http://trailersapi.com/trailers.json?' + urllib.urlencode(parameters))
        #print tmp
        movies = json.loads(response.read())
        #print movies
        print json.dumps(movies)
        return json.dumps(movies)




if __name__ == "__main__":
    app.run()
