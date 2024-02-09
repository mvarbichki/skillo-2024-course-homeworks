class Administrator:

    def __init__(self):
        self.__admin_list = []

    def add_admin(self, admin_name: str):
        self.__admin_list.append(admin_name)

    def if_admin(self, admin_name):
        if admin_name in self.__admin_list:
            return admin_name


class Subscribers:

    def __init__(self):
        self.__subscribers_list = dict()

    def add_subscriber(self, username: str, subscribed: bool):
        self.__subscribers_list.update({username: subscribed})

    # dict guarantee uniq usernames as keys
    def if_subscriber(self, username: str):
        if username in self.__subscribers_list.keys():
            return username

    def is_subscribed(self, username: str):
        return self.__subscribers_list.get(username)
