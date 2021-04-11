from App import app
from flask import request, jsonify
from .movie_model import movies, Movie


@app.route("/api/v1/movies", methods=['GET'])
def get_all_movies():
    all_movies = jsonify(movies)
    return all_movies, 200


@app.route("/api/v1/movies/<int:id>", methods=['GET'])
def get_movie_by_id(id):
    for movie in movies:
        if movie['id'] == id:
            return jsonify(movie), 200
    return jsonify({'message': 'not found'}), 404


@app.route("/api/v1/movies", methods=['POST'])
def create_movie():
    request_data = request.get_json()
    title = request_data['title']
    description = request_data["description"]

    movie = Movie(title=title, description=description).to_json()
    movies.append(movie)
    return jsonify({"message": "movie created successful",
                    "new movie": movie
                    }), 201


@app.route("/api/v1/movies/<int:id>", methods=['DELETE'])
def delete_movie_by_id(id):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
        return jsonify({"message": " movie deleted successfully", "all_movies": movies}), 200
    return jsonify({'message': 'not found'}), 404
