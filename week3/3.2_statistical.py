import math


def mean(s):
    if not s:  # Kiểm tra danh sách rỗng
        return 0
    return sum(s) / len(s)


def variance(s):
    if not s or len(s) < 2:  # Phương sai yêu cầu ít nhất 2 phần tử
        return 0

    m = mean(s)  # Tính giá trị trung bình
    n = len(s)
    sum_squares = sum((x - m) ** 2 for x in s)
    return sum_squares / n


def standarddeviation(s):
    return math.sqrt(variance(s))
