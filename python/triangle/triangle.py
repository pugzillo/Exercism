def is_valid(sides):
    sides.sort()
    if sides[0] + sides[1] >= sides[2] and 0 not in sides:
        return True
    else:
        return False

def is_equilateral(sides):
    if len(set(sides)) == 1 and set(sides) != {0}:
        return True
    return False

def is_isosceles(sides):
    if is_equilateral(sides):
        return True
    if is_valid(sides) and len(set(sides)) == 2:
        return True
    return False


def is_scalene(sides):
    if len(set(sides)) == 3 and is_valid(sides):
        return True
    return False


