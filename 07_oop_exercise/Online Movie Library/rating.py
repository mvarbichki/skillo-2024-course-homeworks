from my_exceptions import RatingCheck


class MovieRating:

    @staticmethod
    def add_rating(movie: object, user: object, rating: int):
        # gets users that gave rating for the current movie
        users_rated = movie.rating.keys()
        try:
            # if user already rated the movie rating is skipped
            if user.username not in users_rated:
                # raises the custom exception if the rating is not between 1 - 5
                if not 0 < rating <= 5:
                    raise RatingCheck("Rating must be between 1 and 5")
                movie.rating.update(
                    {
                        user.username: rating
                    }
                )
                return f"{user.username} rated {movie.title} with: {rating}"
            else:
                return f"{user.username} already rated {movie.title}"
        except RatingCheck as rc:
            return rc
