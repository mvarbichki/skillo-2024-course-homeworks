class UnsuccessfulRequest(Exception):
    def __init__(self, message):
        super().__init__(message)


def is_str(argument):
    if isinstance(argument, str):
        return True
    else:
        return False
