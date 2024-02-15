class OnlineMovieLibrary:

    def __init__(self):
        self.all_movies = {}
        self.admins = []
        self.users = {}

    def add_admin(self, admin: object):
        self.admins.append(admin)
        return f"{admin} created"

    def admin_exist(self, username: str):
        if username in self.admins:
            return username
        else:
            return False

    def add_movie(self, movie: object, admin: str):
        admin = self.admin_exist(admin)
        if admin:
            self.all_movies.update(
                {
                    movie.title: {
                        "description": movie.description
                    }
                }
            )
            return f"{movie.title} added successfully"
        else:
            return "Admin account problem"

    def remove_movie(self, title: str, admin: str):
        admin = self.admin_exist(admin)
        if admin:
            del self.all_movies[title]
            return f"{title} removed"
        else:
            return "Admin account problem"

    def user_exist(self, user: object):
        if user.username in self.users.keys():
            return user.username
        else:
            return False

    def add_user(self, user: object):
        user_exist = self.user_exist(user)
        if not user_exist:
            self.users.update({user.username: user.status})
            return f"{user.username} created"
        else:
            return f"{user.username} already exist"

    def recommended_movies(self):
        return f"Recommended movies: {list(self.all_movies)[-3:]}"

    @staticmethod
    def __if_subscribed(user: object):
        if user.status in ["subscribed", "trial"]:
            return True
        else:
            return False

    def watch_movie(self, movie, user):
        is_subscribed = self.__if_subscribed(user)
        if is_subscribed:
            user.add_to_watched(movie.title)
            return f"{user.username} watching movies: {movie.title}"
        else:
            return f"{user.username} have to subscribe to watch"
