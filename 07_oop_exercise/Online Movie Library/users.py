class Administrator:

    def __init__(self):
        self.__admin_list = []

    def add_admin(self, admin_name: str):
        self.__admin_list.append(admin_name)

    def if_admin(self, admin_name):
        if admin_name in self.__admin_list:
            return admin_name

