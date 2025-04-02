def isMagicSquare(m):
    # Kiểm tra ma trận vuông
    n = len(m)
    for row in m:
        if len(row) != n:
            return False

    # Tính tổng đường chéo chính
    sum_diag1 = 0
    for i in range(n):
        sum_diag1 += m[i][i]

    # Tính tổng đường chéo phụ
    sum_diag2 = 0
    for i in range(n):
        sum_diag2 += m[i][n - 1 - i]

    if sum_diag1 != sum_diag2:
        return False

    magic_sum = sum_diag1

    # Kiểm tra tổng các hàng
    for row in m:
        if sum(row) != magic_sum:
            return False

    # Kiểm tra tổng các cột
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += m[i][j]
        if col_sum != magic_sum:
            return False

    return True


def inputMatrix():
    m = []
    while True:
        line = input().strip()
        if line == "":
            break
        # Tách các số trong hàng bằng dấu tab
        row = list(map(int, line.split('\t')))
        m.append(row)
    return m
