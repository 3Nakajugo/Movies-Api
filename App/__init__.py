from flask import Flask


app = Flask(__name__)
from App.movie import movie_view

