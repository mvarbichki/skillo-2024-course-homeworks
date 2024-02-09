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

"""
class Movie
movie_id:{
    "name": "Rambo",
    "description": "action",
    "rating": avr([{user_id: 3, user_id: 5}])
    }

__init__
    id
    name
    rating




class Movie library
all_movies ={
    Movie obj
}



@admin
def add/remove_movie to/from all_movies(id)
    if i


@user
def calculate_rating()
    return avr(all_movies.get("ratings))
    
@user
def show_movie_info()
    name/descr/calculate_rating()

@user
def show_recomended()
    show last 3 added movie in all_movies




IF ADMIN
-add movie -user_id  movie_id/name/description/rating ADD to all_movies
-remove movie - user_id, movie_id remove from all_movies


IF USER
-if subscibed:
    -accses all_movie | rating | description
    - allowing rate movie ONCE



clas User():

    def select_person(user, list)
    if user in list:
        return user
    else:
        no such user    

class Admins(User):
   admn_list =  {id: name
                }
    
    id
    name
    
 

class Subscriber:
    sub_lst = {
                id:{
                    name: Pencho,
                    status: subscribed
                    },
                id:{
                    name: Toncho,
                    status: subscribed
                    }  
                }
    
    
    id
    name
    status sub/unsub
    
"""
from movies import Movie
from users import Administrator, Subscribers


class OnlineMovieLibrary:
    def __init__(self, library_name: str, library_url: str):
        self.library_name = library_name
        self.library_url = library_url
        self.__all_movies = dict()

    def getter_movies(self):
        return self.__all_movies

    def __find_movie(self, movie_name: str):
        if movie_name in self.__all_movies.keys():
            return movie_name

    def add_movie_to_library(self, movie: dict, admin_name: str):
        # adds movie if provide admin
        admin_exist = admin.if_admin(admin_name)
        if admin_exist:
            self.__all_movies.update(movie)

    def remove_movie_from_library(self, movie_name: str, admin_name: str):
        admin_exist = admin.if_admin(admin_name)
        if admin_exist:
            # if movie exist allow removing
            if self.__find_movie(movie_name):
                del self.__all_movies[movie_name]


library = OnlineMovieLibrary("Movie world", "www.movieworld.com")
admin = Administrator()
admin.add_admin("Stefan")

# create movies obj
m1 = Movie("Rambo-1989", "war, action")
m2 = Movie("Bad Boys-1983", "action")
m3 = Movie("It-2017", "horror")
m4 = Movie("Bad Boys-1995", "action")
m5 = Movie("Love in the air-2024", "romantic, drama")

library.add_movie_to_library(m1.create_movie(), "Stefan")
library.add_movie_to_library(m2.create_movie(), "Stefan")
library.add_movie_to_library(m3.create_movie(), "Stefan")
library.add_movie_to_library(m4.create_movie(), "Stefan")
library.add_movie_to_library(m5.create_movie(), "Stefan")

print(library.getter_movies())
library.remove_movie_from_library("Rambo-1989", "Stefan")
print(library.getter_movies())

s1 = Subscribers()
s1.add_subscriber("someuser1", True)
s1.add_subscriber("someuser2", False)



print(s1.is_subscribed("someuser2"))
