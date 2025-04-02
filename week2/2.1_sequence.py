def isAlt(a):
    if len(a) < 2:
        return False
    for i in range(1, len(a)):
        if (a[i] * a[i - 1]) >= 0:
            return False
    return True


def isGrow(a):
    if len(a) < 2:
        return True
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            return False
    return True


def isMulti(a):
    if len(a) < 2:
        return False
    if 0 in a:
        return False
    ratio = a[1] / a[0]
    for i in range(2, len(a)):
        if abs(a[i] / a[i - 1] - ratio) > 1e-9:
            return False
    return True


def isAdd(a):
    if len(a) < 2:
        return False
    diff = a[1] - a[0]
    for i in range(2, len(a)):
        if a[i] - a[i - 1] != diff:
            return False
    return True
