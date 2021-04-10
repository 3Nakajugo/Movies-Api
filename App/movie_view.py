from App import app
from flask import request, jsonify
from .movie_model import movies, Movie

@app.route("/api/v1/movies", methods=['GET'])
def get_all_movies():
    all_movies = jsonify(todos)
    return all_movies, 200

@app.route("/api/v1/movies", methods=['POST'])
def create_movie():
    request_data = request.get_json()
    title= request_data['title']
    description=request_data["description"]
    
    movie = Movie(title=title,description=description).to_json()
    movies.append(movie)
    return jsonify(movies), 201
