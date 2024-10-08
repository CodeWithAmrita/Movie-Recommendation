import pandas as pd
import csv
from flask import Flask, jsonify, request


#df = pd.read_csv("new.csv")

with open('final.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)

with open('Top_movies.csv', newline="") as f:
  reader = csv.reader(f)
  movies = list(reader)

app = Flask(__name__)

@app.route("/director")
def get_movie_by_director():
    name = request.args.get("director")

    for i in data:
        if i[3] == name:
            return jsonify({
                "data": i[1],
                "message": "success"
                }), 200
            

@app.route("/cast")
def get_movie_by_cast():
    cast = request.args.get("cast")

    for i in data:
        a = i[2].split("'")
        for x in a:
            if x == cast:
                return jsonify({
                "data": i[1],
                "message": "success"
                }), 200

@app.route("/keyword")
def get_movie_by_keyword():
    keyword = request.args.get("keyword")

    for i in data:
        a = i[4].split("'")
        for x in a:
            if x == keyword:
                return jsonify({
                "data": i[1],
                "message": "success"
                }), 200

@app.route("/genre")
def get_movie_by_genre():
    genre = request.args.get("genre")

    for i in data:
        a = i[5].split("'")
        for x in a:
            if x == genre:
                return jsonify({
                "data": i[1],
                "message": "success"
                }), 200

@app.route("/topmovies")
def top_movies():
    
    for i in movies:
        return jsonify({
            "data": movies,
            "message": "success"
            }), 200


if __name__ == "__main__":
    app.run()


#get_movie_by_director("James Cameron")
#get_movie_by_cast("Marty")
#get_movie_by_keyword("culture clash")
#get_movie_by_genre("Science Fiction")






    

