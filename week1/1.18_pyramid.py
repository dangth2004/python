def leftHalfPyramid(n):
    for i in range(1, n + 1):
        print('*' * i)


def rightHalfPyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)


def fullPyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def invertedFullPyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def hollowPyramid(n):
    for i in range(1, n + 1):
        if i == 1:
            print(' ' * (n - i) + '*')
        elif i == n:
            print('*' * (2 * n - 1))
        else:
            print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')
