# Hoàn thiện hàm is_palindrome(p), hàm này thực hiện kiểm tra số nguyên p có phải là số đối xứng hay không, nếu có thì trả lại giá trị True, và ngược lại thì trả lại giá trị False.
def is_palindrome(p):
    n = p
    result = 0
    while n > 0:
        result = result * 10 + (n % 10)
        n //= 10
    return result == p
