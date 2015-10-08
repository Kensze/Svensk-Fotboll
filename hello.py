import urllib2
import urllib
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/update")
def search():
	query = "star wars"
	parameters = {'s' : query, 'r' : 'json'}
	# Fetches the result from the API
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	movies = json.loads(response.read())
	#return render_template("search_results.html", data = search)
	return jsonify(movies)


if __name__ == "__main__":
    app.run()