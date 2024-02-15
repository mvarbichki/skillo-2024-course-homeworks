# custom check for the rating
class RatingCheck(Exception):
    def __init__(self, message):
        super().__init__(message)