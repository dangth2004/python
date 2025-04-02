def isPerfectNumber(number: int):
    """
    Số hoàn hảo là một số nguyên dương mà tổng các ước nguyên dương thực sự của nó
    (các ước nguyên dương ngoại trừ chính số đó) bằng chính nó. Hoàn thiện hàm isPerfectNumber(number)
    nhận vào số nguyên dương number và trả về True nếu number là số hoàn hảo
    và False nếu number không phải là số hoàn hảo.

    Ví dụ:
    input: 6
    ouput: True

    input: 14
    output: False
    """
    if number <= 1:
        return False
    sum_divisors = 1  # 1 là ước của mọi số
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum_divisors += i
            if i != number // i:  # Tránh trường hợp số chính phương cộng 2 lần
                sum_divisors += number // i
    return sum_divisors == number


def drawPatterm(height: int):
    """
    Hãy vẽ hình vuông có chiều cao height.
    Ví dụ
    input: 4
    output:
    ****
    *  *
    *  *
    ****
    """
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * height)
        else:
            print('*' + ' ' * (height - 2) + '*')


def caculateExp(x: float, n: int):
    """
    Hoàn thiện hàm tính e^x theo công thức đã cho của đề bài.
    Ví dụ:
    input: 2 100 (Tương ứng x = 2 và n = 100)
    output: 7.3890561
    """
    result = 1.0  # Term đầu tiên (khi i=0): x^0 / 0! = 1
    term = 1.0  # Lưu giá trị của term hiện tại để tính term tiếp theo
    for i in range(1, n + 1):
        term *= x / i  # term_i = term_{i-1} * (x / i)
        result += term
    return result
