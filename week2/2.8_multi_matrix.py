def inputMatrix():
    m = []
    rows, cols = map(int, input().split())
    for _ in range(rows):
        row = list(map(int, input().split()))
        m.append(row)
    return m


def multiMatrix(m1, m2):
    # Kiểm tra kích thước ma trận
    if len(m1[0]) != len(m2):
        print("Không thể nhân hai ma trận với kích thước này!")
        return None

    # Khởi tạo ma trận kết quả với giá trị 0
    r = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    # Thực hiện phép nhân ma trận
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                r[i][j] += m1[i][k] * m2[k][j]
    return r


def printMatrix(m):
    if m is None:
        return
    for row in m:
        print(' '.join(map(str, row)))


m1 = inputMatrix()
m2 = inputMatrix()

mm = multiMatrix(m1, m2)
printMatrix(mm)
