from datetime import date

movies = [
    {
        "id": 1,
        "title": "hello",
        "description": "mlcmlodaflamclxzmcopd",
        "release_date": "16/09/2019",
        "director": "edna"

    }
]


class Movie:
    def __init__(self, title, description, release_date, language, director):
        self.id = len(movies)+1
        self.title = title
        self.description = description
        self.release_date = date.today()
        self.language = language
        self.director = director

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "release_date": self.release_date,
            "language": self.language,
            "director": self.director
        }
