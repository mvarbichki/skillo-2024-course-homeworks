from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def create_account(self, *args):
        pass

    @abstractmethod
    def if_user(self, username):
        pass


class Administrator(User):

    def __init__(self):
        self.__admin_list = set()

    def create_account(self, username: str):
        if username not in self.__admin_list:
            self.__admin_list.add(username)
            return f"{username} created"
        else:
            return f"{username} already exist"

    def if_user(self, username: str):
        if username in self.__admin_list:
            return username


class Subscribers(User):

    def __init__(self):
        self.__subscribers_list = dict()

    # adds sub in a dict. Each sub has own sub status, watched list, favorites list
    def create_account(self, username: str, sub_status: str):
        if username not in self.__subscribers_list.keys():
            self.__subscribers_list.update(
                {username: {"status": sub_status,
                            "watched": [],
                            "favorites": []
                            }
                 }
            )
            return f"{username} created"
        else:
            return f"{username} already exist"

    def if_user(self, username: str):
        if username in self.__subscribers_list:
            return username

    def is_subscribed(self, username: str):
        sub = self.__get_subscriber(username)
        if sub.get("status") in ["subscribed", "trial"]:
            return True
        else:
            return False

    def get_subscribers(self):
        return self.__subscribers_list

    # helper method for finding teh sub
    def __get_subscriber(self, subscriber: str):
        if subscriber in self.__subscribers_list.keys():
            return self.__subscribers_list.get(subscriber)

    def add_to_watched(self, subscriber: str, movie_name: str):
        sub = self.__get_subscriber(subscriber)
        sub.get("watched").append(movie_name)

    def add_to_favorites(self, subscriber: str, movie_name: str):
        sub = self.__get_subscriber(subscriber)
        sub.get("favorites").append(movie_name)

    def if_watched(self, subscriber: str, movie_name: str):
        sub = self.__get_subscriber(subscriber)
        if movie_name in sub.get("watched"):
            return True
        else:
            return False
