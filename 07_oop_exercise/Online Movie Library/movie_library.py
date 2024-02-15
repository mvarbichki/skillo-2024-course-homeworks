class OnlineMovieLibrary:

    def __init__(self):
        self.__all_movies = {}
        self.__admins = []
        self.__users = {}

        # calculating avr rating for movie

    @staticmethod
    def __average_rating(ratings: list):
        # if no rating returns 0. If rating calculate avg rating
        try:
            return sum(ratings) / len(ratings)
        except ZeroDivisionError:
            return 0

    def show_all_movies(self):
        movies_list = []
        # unpacks keys and values
        for k, v in self.__all_movies.items():
            # calculates avg rating for each movie
            rating = str(self.__average_rating(list(v.get("rating").values())))
            movies_list.append("Movie: " + k + " | Description: " + v.get("description") + " | Rating: " + rating)
        return movies_list

    def add_admin(self, admin: object):
        self.__admins.append(admin)
        return f"{admin} created"

    def admin_exist(self, username: str):
        if username in self.__admins:
            return username
        else:
            return False

    def add_movie(self, movie: object, admin: str):
        admin = self.admin_exist(admin)
        if admin:
            self.__all_movies.update(
                {
                    movie.title: {
                        "description": movie.description,
                        "rating": movie.rating
                    }
                }
            )
            return f"{movie.title} added successfully"
        else:
            return "Admin account problem"

    def remove_movie(self, title: str, admin: str):
        admin = self.admin_exist(admin)
        if admin:
            del self.__all_movies[title]
            return f"{title} removed"
        else:
            return "Admin account problem"

    def user_exist(self, user: object):
        if user.username in self.__users.keys():
            return user.username
        else:
            return False

    def add_user(self, user: object):
        user_exist = self.user_exist(user)
        if not user_exist:
            self.__users.update({user.username: user.status})
            return f"{user.username} created"
        else:
            return f"{user.username} already exist"

    def recommended_movies(self):
        # returns the last 3 records as recommended
        return f"Recommended movies: {list(self.__all_movies)[-3:]}"

    # helper for sub status
    @staticmethod
    def __if_subscribed(user: object):
        if user.status in ["subscribed", "trial"]:
            return True
        else:
            return False

    def watch_movie(self, movie: object, user: object):
        is_subscribed = self.__if_subscribed(user)
        # if user subscribed/trial can watch
        if is_subscribed:
            user.add_to_watched(movie.title)
            return f"{user.username} watching movies: {movie.title}"
        else:
            return f"{user.username} have to subscribe to watch"
