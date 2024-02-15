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

from movie_library import OnlineMovieLibrary
from movies import Movie
from users import Administrator, User

movie_library = OnlineMovieLibrary()
admin = Administrator("someadmin")
print(movie_library.add_admin(admin.username))

movie_one = Movie(title="Rambo-1987", description="war, action")
movie_two = Movie(title="Bad boys-1995", description="comedy, action")
movie_three = Movie(title="Ace age-2012", description="comedy, animation")
movie_four = Movie(title="Bad boys-1983", description="comedy, action")
movie_five = Movie(title="It-2019", description="horror")
movie_six = Movie(title="Love is in the air-2022", description="romantic")

print(movie_library.add_movie(movie_one, "someadmin"))
print(movie_library.add_movie(movie_two, "someadmin"))
print(movie_library.add_movie(movie_three, "someadmin"))
print(movie_library.add_movie(movie_four, "someadmin"))
print(movie_library.add_movie(movie_five, "wrongadmin"))
print(movie_library.add_movie(movie_five, "someadmin"))
print(movie_library.add_movie(movie_six, "someadmin"))

print(movie_library.all_movies)
print(movie_library.remove_movie("Rambo-1987", "someadmin"))
print(movie_library.all_movies)

user_one = User("someuser_one", "subscribed")
user_two = User("someuser_two", "trial")
user_three = User("someuser_three", "not subscribed")
user_four = User("someuser_two", "not subscribed")
print(movie_library.recommended_movies())

print(movie_library.add_user(user_one))
print(movie_library.add_user(user_two))
print(movie_library.add_user(user_three))
print(movie_library.add_user(user_four))

print(movie_library.watch_movie(movie_four, user_three))
print(movie_library.watch_movie(movie_three, user_two))
print(movie_library.watch_movie(movie_six, user_two))

print(user_two.show_watched())


print(user_two.add_to_favorites(movie_three))
print(user_two.add_to_favorites(movie_three))
print(user_two.show_favorites())
