from math import sqrt


def function(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError
    if a == 0:
        raise Exception('a=0')
    d = b * b - 4 * a * c
    if d > 0:
        return [int(-b + sqrt(d) / 2 * a), int(-b - sqrt(d) / 2 * a)]
    elif d == 0:
        return [-b / 2 * a]
    else:
        return []
