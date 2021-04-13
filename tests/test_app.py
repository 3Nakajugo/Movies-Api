import unittest
import json
from App import app
from App.movie_model import Movie, movies


class TestMovieApi(unittest.TestCase):
    """ Class tests Movie api"""

    def setUp(self):
        self.client = app.test_client()
        self.new_movie = {
            "title": "ee",
            "description": "mlcmlodaflamclxzmcopd",
            "release_date": "16/09/20202",
            "language": "english",
            "director": "edna"
        }

    def tearDown(self):
        movies.clear()

    def test_get_all_movies_success(self):
        response = self.client.get("/api/v1/movies")
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_data), 1)

    def test_get_movie_by_id_success(self):
        response = self.client.post(
            "/api/v1/movies", json=self.new_movie)
        response = self.client.get("/api/v1/movies/1")
        self.assertEqual(response.status_code, 200)

    def test_get_movie_by_id_fails(self):
        response = self.client.get("/api/v1/movies/3")
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data['message'], "not found")

    def test_create_movie(self):
        response = self.client.post(
            "/api/v1/movies", content_type='application/json',  data=json.dumps(self.new_movie))
        response_data = json.loads(response.data)
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "movie created successful")


if __name__ == '__main__':
    unittest.main()
