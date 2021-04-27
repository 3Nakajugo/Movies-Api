from flask import Flask


app = Flask(__name__)
from App.movie import movie_view
from App.auth import user_view

