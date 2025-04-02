# Chương trình in tam giác PASCAL
def print_pascal_triangle(m):
    for i in range(m + 1):
        row = []
        for j in range(i + 1):
            # Tính C(i, j)
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(row[j - 1] * (i - j + 1) // j)
        # In dòng với định dạng yêu cầu
        print(' '.join(map(str, row)) + ' ')


# Nhập m từ input
m = int(input())
print_pascal_triangle(m)
