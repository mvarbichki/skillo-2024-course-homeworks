# my exceptions
class IsAlphabetic(Exception):
    def __init__(self, message):
        super().__init__(message)


class InRange(IsAlphabetic):
    pass
