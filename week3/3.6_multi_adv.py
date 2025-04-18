def multiplyDigit(num, digit):
    """Nhân một số (dạng list) với một chữ số (0-9)"""
    if digit == 0:
        return [0]

    carry = 0
    result = []
    for d in reversed(num):
        product = d * digit + carry
        result.append(product % 10)
        carry = product // 10

    if carry > 0:
        result.append(carry)

    return result[::-1]


def addNumbers(x, y):
    """Cộng hai số (dạng list)"""
    # Đảo ngược để tính từ phải sang trái
    x_rev = x[::-1]
    y_rev = y[::-1]

    # Cân bằng độ dài
    max_len = max(len(x_rev), len(y_rev))
    x_rev += [0] * (max_len - len(x_rev))
    y_rev += [0] * (max_len - len(y_rev))

    carry = 0
    result = []
    for a, b in zip(x_rev, y_rev):
        total = a + b + carry
        result.append(total % 10)
        carry = total // 10

    if carry > 0:
        result.append(carry)

    # Đảo ngược lại và loại bỏ số 0 thừa ở đầu
    result = result[::-1]
    while len(result) > 1 and result[0] == 0:
        result = result[1:]

    return result


def multiNum(a, b):
    """Nhân hai số (dạng list)"""
    if a == [0] or b == [0]:
        return [0]

    total = [0]

    # Duyệt từ phải sang trái của b
    for i, digit in enumerate(reversed(b)):
        # Nhân a với chữ số hiện tại của b
        partial = multiplyDigit(a, digit)

        # Thêm các số 0 tương ứng với vị trí
        partial += [0] * i

        # Cộng vào tổng
        total = addNumbers(total, partial)

    return total
