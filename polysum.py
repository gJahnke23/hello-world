import math

def polysum(n, s):
    '''
    :param n: Number of sides
    :param s: length of sides
    :return: Sums the area and square of the perimeter ofa regular polygon, roudned to 4 places
    '''
    sqrper = (n * s) ** 2
    area = (.25 * n * s ** 2) / math.tan(math.pi / n)
    return round(sqrper + area, 4)
