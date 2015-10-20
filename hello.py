import urllib2
import urllib
import json
from flask import Flask, render_template, jsonify, request
from flask.ext.cors import CORS, cross_origin
from flask.ext.triangle import Triangle

app = Flask(__name__, static_path='/static')
Triangle(app)
CORS(app)
#app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/movie/<ID>")
def movie(ID):
    return render_template("movie.html")

#@app.route('/trailers/<id>')
#def trailers(id):
#        parameters = {'imdb' : id, 'count' : 1, 'format' : 'json' }
#        response = urllib2.urlopen('http://www.myapifilms.com/taapi?' + urllib.urlencode(parameters))
        #print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
#        movies = json.loads(response.read())
#        return jsonify(movies)



@app.route("/update", methods=['POST', 'GET'])
def search():
        post = request.get_json()
        query = post.get('search')
        parameters = {'s' : query, 'r' : 'json'}
        response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
        #print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
        movies = json.loads(response.read())
        return jsonify(movies)

@app.route('/movies/<id>')
def view(id):
        parameters = {'i' : id, 'plot' : 'short', 'r' : 'json'}
        response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
        #print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
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
        #print json.dumps(movies)
        return json.dumps(movies)




if __name__ == "__main__":
    app.run()
