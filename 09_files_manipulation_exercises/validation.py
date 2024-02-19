class IsAlphabetic(Exception):
    def __init__(self, message):
        super().__init__(message)


class IsScoreRange(IsAlphabetic):
    pass


def inputs_check(name, score):
    try:
        float_score = float(score)
        # allows alphabetic for the name
        if not name.isalpha():
            raise IsAlphabetic("Name have to be alphabetic")
        # allows float score in range 1 to 10
        if not 1 <= float_score <= 10:
            raise IsScoreRange("Score have to be between 1 and 10")
    except ValueError:
        return "Score have to be float"
    except IsScoreRange as isr:
        return isr
    except IsAlphabetic as ia:
        return ia
    # if no exceptions return true
    else:
        return True
