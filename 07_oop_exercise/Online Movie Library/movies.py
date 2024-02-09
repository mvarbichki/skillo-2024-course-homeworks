class Movie:
    def __init__(self, movie_name: str, description: str):
        self.movie_name = movie_name
        self.description = description
        self.rating = []

    # the key will combine the movie name and the year. Simple solution to avoid duplication
    def create_movie(self):
        return {
            self.movie_name: {
                "description": self.description,
                "rating": self.rating
            }
        }
