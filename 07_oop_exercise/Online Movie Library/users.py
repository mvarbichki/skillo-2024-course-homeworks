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

    def create_account(self, username: str, subscribed: str):
        if username not in self.__subscribers_list.keys():
            self.__subscribers_list.update({username: subscribed})
            return f"{username} created"
        else:
            return f"{username} already exist"

    def if_user(self, username: str):
        if username in self.__subscribers_list:
            return username

    def is_subscribed(self, username: str):
        if self.__subscribers_list.get(username) in ["subscribed", "trial"]:
            return True
        else:
            return False
