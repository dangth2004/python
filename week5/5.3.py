import math


def is_prime(n):
    """Kiểm tra xem số n có phải là số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sum_digits(n):
    """Tính tổng các chữ số của số n"""
    return sum(int(d) for d in str(abs(n)))


def findLuckyNumber(filename):
    """Tìm và trả về số may mắn trong file văn bản"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Tách các token trong dòng
            tokens = line.split()
            for token in tokens:
                # Kiểm tra nếu token là số nguyên
                if token.lstrip('-').isdigit():
                    num = int(token)
                    # Kiểm tra số may mắn: nguyên tố và tổng chữ số chia hết cho 5
                    if is_prime(num) and sum_digits(num) % 5 == 0:
                        return num
    return 0  # Trả về 0 nếu không tìm thấy
