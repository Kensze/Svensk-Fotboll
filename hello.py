# -*- coding: utf-8 -*-

import collections

import urllib2
import urllib
import json
from flask import Flask, render_template, jsonify, request
from flask.ext.cors import CORS, cross_origin
from flask.ext.triangle import Triangle

app = Flask(__name__, static_path='/static')
cors = CORS(app, allow_headers='Content-Type', CORS_SEND_WILDCARD=True)
app.config['CORS_HEADERS'] = 'Content-Type'
Triangle(app)
app.debug = True


#Routen för första sidan som renderar index templaten
@app.route("/")
@cross_origin(origins='*', send_wildcard=True)
def hello():
    return render_template("index.html")

#Route för en film och dess id, en template renderas. I templaten finns javascript som hämtar information
@app.route("/film/<ID>")
@cross_origin(origins='*', send_wildcard=True)
def movie(ID):
    return render_template("movie.html")

#Hämtar data om en viss trailer som tillhör en film i JSON format från omdb api
'''
@app.route('/trailer/<id>')
def trailers(id):
        parameters = {'imdb' : id, 'count' : 1, 'format' : 'json' }
        response = urllib2.urlopen('http://www.myapifilms.com/taapi?' + urllib.urlencode(parameters))
        movies = json.loads(response.read())
        if not movies:
            return jsonify({"Error": "Incorrect IMDb ID", "Response": "False"})
        return jsonify(movies)
'''


#Hämtar en lista på sökresultat av en filmtitel genom ett api i JSON format
@app.route("/search", methods=['POST', 'GET', 'OPTIONS'])
@cross_origin(origins='*', send_wildcard=True)
def search():
    	post = request.get_json()
	query = post.get('search').encode('utf8')
	parameters = {'s' : query, 'r' : 'json'}
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	movies = json.loads(response.read())
        if not movies:
            return jsonify({"Error": "Inga filmer hittade"})
	return jsonify(movies)


#Hämtar information om en film genom omdb api
@app.route('/movie/<id>')
@cross_origin(origins='*', send_wildcard=True)
def view(id):
    	parameters = {'i' : id, 'plot' : 'short', 'r' : 'json'}
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	movies = json.loads(response.read())

	if not movies:
            return jsonify({"Error": "Ingen film med det id"})

        for elem in movies:
            r = dict(movies)
	    if r['Awards']:
		del r['Awards']
	    if r['Country']:
		del r['Country']
	    if r['Director']:
		del r['Director']
	    if r['Genre']:
		del r['Genre']
	    if r['Language']:
		del r['Language']
	    if r['Metascore']:
		del r['Metascore']
	    if r['Poster']:
		del r['Poster']
	    if r['Rated']:
		del r['Rated']
	    if r['Released']:
		del r['Released']
	    if r['Response']:
		del r['Response']
	    if r['Runtime']:
		del r['Runtime']
	    if r['Type']:
		del r['Type']
	    if r['Year']:
		del r['Year']
	    if r['imdbRating']:
		del r['imdbRating']
	    if r['idmbVotes']:
		del r['imdbVotes']


        parameters = {'imdb' : id, 'count' : 1, 'format' : 'json' }
        response = urllib2.urlopen('http://www.myapifilms.com/taapi?' + urllib.urlencode(parameters))
        trailer = json.loads(response.read())
	if trailer:
	    embed = trailer['trailer'][0]['embed']
	    link = trailer['trailer'][0]['link']

	    r['trailer_embed'] = embed
            r['trailer_link'] = link

	else:
	 r['trailer_embed'] = "Not Found"
	 r['trailer_link'] = "Not Found"

        return jsonify(r)

if __name__ == "__main__":
    app.run()
