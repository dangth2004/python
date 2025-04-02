def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        row = list(map(int, line.split()))
        m.append(row)

    # Kiểm tra tính vuông của ma trận
    n = len(m)
    for row in m:
        if len(row) != n:
            print("Lỗi: Ma trận không vuông! Vui lòng nhập lại.")
            return inputMatrix()
    return m


def isUpperTriangleMatrix(m):
    n = len(m)
    for i in range(n):
        for j in range(i):  # Kiểm tra các phần tử dưới đường chéo chính
            if m[i][j] != 0:
                return False
    return True


m = inputMatrix()
print(isUpperTriangleMatrix(m))
