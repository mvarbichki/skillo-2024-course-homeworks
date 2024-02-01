from math import pi


def area_of_square(a):
    # checks if argument is numeric
    if (isinstance(a, float)) or (isinstance(a, int)):
        # checks if numeric is positive
        if a < 1:
            return "Argument should be positive numeric"
        return a * a
    else:
        return "Wrong argument type"


def area_of_rectangle(length, width):
    # checks if arguments are numeric
    if (isinstance(length, int) or isinstance(length, float)) and (isinstance(width, int) or isinstance(width, float)):
        # checks if numerics are positive
        if (length < 1) or (width < 1):
            return "Arguments should be positive numeric"
        return length * width
    else:
        return "Wrong arguments type"


def area_of_triangle(base, height):
    # checks if arguments are numeric
    if (isinstance(base, int) or isinstance(base, float)) and (isinstance(height, int) or isinstance(height, float)):
        if (base < 1) or (height < 1):
            # checks if numerics are positive
            return "Arguments should be positive numerics"
        return (base * height) / 2
    else:
        return "Wrong arguments type"


def area_of_circle(radius):
    # checks if argument is numeric
    if (isinstance(radius, int)) or isinstance(radius, float):
        # checks if argument is positive
        if radius < 1:
            return "Argument should be positive numeric"
        # using built-in pow and math lyb pi to calculate the area
        area = pi * pow(radius, 2)
        # returns the result formatted to two digits after the decimal
        return "%.2f" % area
    else:
        return "Wrong argument type"
