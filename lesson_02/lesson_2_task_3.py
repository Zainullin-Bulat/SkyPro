import math


def square(side):
    area = side * side
    if side == int(side):
        return int(area)
    else:
        return math.ceil(area)


print(square(2.1))
