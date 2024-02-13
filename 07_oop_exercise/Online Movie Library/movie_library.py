"""Problem 1:
Implement an online movie library like Netflix. It should have users, admins that can
add/remove content, subscriptions with trial period, movies.
Every user should be able to add a movie in list of favourites. They should also be able to get a
list of recommended movies (at least 3) (( Could be the last 3 added)).
They should be able to mark movies as watched and also rate the movie with a rating ranging 1
to 5. Users should be able to get a list of all watched movies.
Organize your code in modules and follow the good OOP principles.
Start with designing your classes and entities in the project.
**Tasks:**
1. Create the classes mentioned above, ensuring appropriate encapsulation and data validation where necessary.
2. Demonstrate the system's functionality by simulating interactions such as watching a movie, asking for
 recommendations, marking a movie as watched, rating a movie, listing all watched movies and so on.
3. Implement tests cases accordingly"""

from movies import Movie
from users import Administrator, Subscribers


class OnlineMovieLibrary:
    def __init__(self, library_name: str, library_url: str):
        self.library_name = library_name
        self.library_url = library_url
        self.__all_movies = dict()

    # everyone could see what library contains
    def show_all_lib_movies(self):
        movies = []
        for k, v in self.__all_movies.items():
            movies.append("Movie: " + k + " | Description: " + v.get("description") + " | Rating: " + str(self.__average_rating(v.get("rating"))))
            #print(k, v.get("description"),  self.__average_rating(v.get("rating")))
        return movies

    # helper for finding movie
    def __get_movie(self, movie_name: str):
        if movie_name in self.__all_movies.keys():
            return self.__all_movies.get(movie_name)

    @staticmethod
    def __average_rating(ratings: list):
        try:
            return sum(ratings) / len(ratings)
        except ZeroDivisionError:
            return 0

    def add_movie_to_library(self, movie: dict, admin_user: str):
        # adds movie if provide admin
        admin_exist = admin.if_user(admin_user)
        if admin_exist:
            self.__all_movies.update(movie)
            return f"{movie.keys()} added successfully"
        else:
            return "Incorrect admin"

    def remove_movie_from_library(self, movie_name: str, admin_name: str):
        admin_exist = admin.if_user(admin_name)
        if admin_exist and self.__get_movie(movie_name):
            del self.__all_movies[movie_name]
            return f"{movie_name} removed"
        else:
            return "Incorrect admin "

    def show_recommended_movies(self, subscriber: str):
        # converts dict to list and show the last 3 elements
        recently_added_movies = list(self.__all_movies.items())[-3:]
        registered_sub = subscribers.if_user(subscriber)
        # any registered sub can see recommended movies
        if registered_sub:
            return f"Recommended: {recently_added_movies}"
        else:
            return f"You need to create account"

    def watch_movie(self, subscriber: str, movie_name: str):
        subscribed_or_trial = subscribers.is_subscribed(subscriber)
        movie_exist = self.__get_movie(movie_name)
        # sub can watch movie if it exists and subscribed/trial
        if movie_exist and subscribed_or_trial:
            subscribers.add_to_watched(subscriber, movie_name)
            return f"{subscriber} watched {movie_name}"
        else:
            return "You need to subscribe"

    def mark_favorites(self, subscriber: str, movie_name: str):
        subscribed_or_trial = subscribers.is_subscribed(subscriber)
        movie_exist = self.__get_movie(movie_name)
        # sub can add to own favorite list if movie exist, subscribed/trial
        if movie_exist and subscribed_or_trial:
            subscribers.add_to_favorites(subscriber, movie_name)
            return f"{subscriber} added {movie_name} to favorites"
        else:
            return "You need to subscribe"

    def rating_a_movie(self, subscriber: str, movie_name: str, rating: int):
        hes_been_watched = subscribers.if_watched(subscriber, movie_name)
        subscribed_or_trial = subscribers.is_subscribed(subscriber)
        if hes_been_watched and subscribed_or_trial:
            movie_to_rate = self.__get_movie(movie_name)
            movie_to_rate.get("rating").append(rating)

    # TODO
    #   def calculate_rating()
    #   def give_rating


library = OnlineMovieLibrary("Movie world", "www.movieworld.com")
admin = Administrator()
print(admin.create_account("someadmin"))
print(admin.create_account("someadmin"))
subscribers = Subscribers()

# create movies obj
m1 = Movie("Rambo-1994", "war, action")
m2 = Movie("Bad Boys-1983", "action")
m3 = Movie("It-2017", "horror")
m4 = Movie("Bad Boys-1995", "action")
m5 = Movie("Love in the air-2024", "romantic, drama")
m_six = Movie("Ace age-2012", "animation, family")

print(library.add_movie_to_library(m1.create_movie(), "someadmin"))
print(library.add_movie_to_library(m2.create_movie(), "someadmin"))
print(library.add_movie_to_library(m3.create_movie(), "someadmin"))
print(library.add_movie_to_library(m4.create_movie(), "someadmin"))
print(library.add_movie_to_library(m5.create_movie(), "someadmin"))
print(library.add_movie_to_library(m_six.create_movie(), "someadmin"))
print(library.add_movie_to_library(m_six.create_movie(), "someadminp"))

print(library.show_all_lib_movies())
print(library.remove_movie_from_library("Rambo-1994", "someadmin"))
print(library.show_all_lib_movies())

print(subscribers.create_account("someuser1", "subscribed"))
print(subscribers.create_account("someuser2", "trial"))
print(subscribers.create_account("someuser3", "not subscribed"))
print(subscribers.create_account("someuser3", "not subscribed"))

print(library.show_recommended_movies('someuser'))
print(library.show_recommended_movies('someuser3'))

print(library.watch_movie("someuser1", "It-2017"))
print(library.watch_movie("someuser1", "Love in the air-2024"))
print(library.watch_movie("someuser2", "It-2017"))
print(library.watch_movie("someuser3", "It-2017"))

print(library.mark_favorites("someuser1", "It-2017"))
print(library.mark_favorites("someuser1", "Love in the air-2024"))
print(library.mark_favorites("someuser2", "Bad Boys-1995"))
print(library.mark_favorites("someuser3", "Bad Boys-1995"))

print(library.show_all_lib_movies())
library.rating_a_movie("someuser1", "It-2017", 4)
library.rating_a_movie("someuser1", "It-2017", 3)
print(library.show_all_lib_movies())
