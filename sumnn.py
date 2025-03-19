# Viết chương trình cho phép nhập một số nguyên n từ bàn phím
# tính và in ra kết quả của biểu thức n + nn + nnn + nnnn
# Ví dụ n = 5, kết quả là 5 + 55 + 5555 + 5555 = 6170
# Chú ý: n có thể là số tự nhiên bất kỳ
def num_length(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


def sum(number):
    n = number
    sum = 0
    for i in range(1, 5):
        sum += number
        number = number * (10 ** num_length(n)) + n
    return sum


number = int(input())
print(sum(number))
