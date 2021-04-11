movies = [
    {
        "id": 1,
        "title": "hello",
        "description": "mlcmlodaflamclxzmcopd"
    },
    {
        "id": 2,
        "title": "hello",
        "description": "mlcmlodaflamclxzmcopd"
    }
]


class Movie:
    def __init__(self, title, description):
        self.id = len(movies)+1
        self.title = title
        self.description = description

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
