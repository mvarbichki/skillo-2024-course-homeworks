class Movie:
    def __init__(self, movie_name: str, description: str):
        self.movie_name = movie_name
        self.description = description
        self.rating = []

    def create_movie(self):
        return {
            self.movie_name: {
                "description": self.description,
                "rating": self.rating
            }
        }
