import urllib2
import urllib
import json
from flask import Flask, render_template, jsonify, request
from flask.ext.cors import CORS, cross_origin
from flask.ext.triangle import Triangle


#from flask.ext import restful
#from flask.ext.restful import Api


app = Flask(__name__, static_path='/static')
cors = CORS(app, allow_headers='Content-Type', CORS_SEND_WILDCARD=True)
app.config['CORS_HEADERS'] = 'Content-Type'
Triangle(app)
#api = restful.Api(app)
#app = Flask(__name__)
app.debug = True

"""@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response"""




@app.route("/")
@cross_origin(origins='*', send_wildcard=True)
def hello():
    return render_template("index.html")

@app.route("/movie/<ID>")
@cross_origin(origins='*', send_wildcard=True)
def movie(ID):
    return render_template("movie.html")

@app.route('/trailers/<id>')
def trailers(id):
        parameters = {'imdb' : id, 'count' : 1, 'format' : 'json' }
        response = urllib2.urlopen('http://www.myapifilms.com/taapi?' + urllib.urlencode(parameters))
	print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
        movies = json.loads(response.read())
        if not movies:
            return jsonify({"Error": "Incorrect IMDb ID", "Response": "False"})
        return jsonify(movies)



@app.route("/update", methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(origins='*', send_wildcard=True)
def search():
    	post = request.get_json()
	query = post.get('search')
	parameters = {'s' : query, 'r' : 'json'}
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	#print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
	movies = json.loads(response.read())
	return jsonify(movies)

@app.route('/movies/<id>')
@cross_origin(origins='*', send_wildcard=True)
def view(id):
    	parameters = {'i' : id, 'plot' : 'short', 'r' : 'json'}
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	#print 'http://www.omdbapi.com/?' + urllib.urlencode(parameters)
	movies = json.loads(response.read())
	return jsonify(movies)


@app.route('/trailer', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(origins='*', send_wildcard=True)
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
