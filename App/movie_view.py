from App import app
from flask import request, jsonify
from .movie_model import movies, Movie


@app.route("/api/v1/movies", methods=['GET'])
def get_all_movies():
    if len(movies) > 0:
        all_movies = jsonify(movies)
        return all_movies, 200
    return jsonify({"message": "no movies to display"})


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
    description = request_data['description']
    release_date = request_data['release_date']
    language = request_data['language']
    director = request_data['director']

    movie = Movie(title=title, description=description, release_date=release_date,
                  language=language, director=director).to_json()
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
        return jsonify({'error': 'movie not found'}), 404


@app.route("/api/v1/movies/<int:id>", methods=['PUT'])
def update_movie_by_id(id):
    request_data = request.get_json()

    for movie in movies:
        if movie['id'] == id:
            title = request_data['title']
            description = request_data["description"]
            release_date = request_data['release_date']
            language = request_data['language']
            director = request_data['director']
            movie.update(title=title, description=description, release_date=release_date,
                         language=language, director=director)
            return jsonify({"message": " movie updated successfully", "all_movies": movie}), 200
        return jsonify({'error': 'not found'}), 404
