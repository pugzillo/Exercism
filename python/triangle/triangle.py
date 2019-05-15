def is_equilateral(sides):
    if len(set(sides)) == 1 and set(sides) != {0}:
        return True
    return False


def is_isosceles(sides):
    if len(set(sides)) == 1 or len(set(sides)) == 2:
        # Check inequality
        triangle = dict()   # dict with sides len and number of sides with that length
        for i in sorted(sides):
            triangle[i] = triangle.get(i, 0) + 1
        legs = 0
        base = 0
        for k, v in triangle.items():   # identify legs and base
            if v == 2:
                legs = k
            if v == 1:
                base = k

        if 2*legs >= base:
            return True
    return False


def is_scalene(sides):
    if len(set(sides)) == 3:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False


# print(is_isosceles([1, 1, 3]))
# print(is_isosceles([4, 4, 3]))