def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        row = list(map(int, line.split()))
        m.append(row)
    return m


def transpose(m):
    n = len(m)
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = m[i][j]
    return t


def printMatrix(t):
    print("\nMa trận chuyển vị:")
    for row in t:
        print(' '.join(map(str, row)))


m = inputMatrix()
t = transpose(m)
printMatrix(t)
