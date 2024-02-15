from movie_library import OnlineMovieLibrary


class Administrator:
    def __init__(self, username: str):
        self.username = username


class User:
    def __init__(self, username: str, status: str):
        self.username = username
        self.status = status
        self.__favorites = []
        self.__watched = []

    def add_to_favorites(self, movie: object):
        if movie.title not in self.__favorites:
            self.__favorites.append(movie.title)
            return f"{self.username} added {movie.title} to favorites"
        else:
            return f"{movie.title} already in favorites"

    def add_to_watched(self, movie: str):
        if movie not in self.__watched:
            self.__watched.append(movie)

    def show_watched(self):
        return f"{self.username} watched movies: {self.__watched}"

    def show_favorites(self):
        return f"{self.username} favorites movies: {self.__favorites}"
