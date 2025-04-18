# Nhập hai số nguyên từ bàn phím
a = int(input())
b = int(input())

# Tìm các số chia hết cho 11 nhưng không chia hết cho 3
result = []
for num in range(a, b + 1):
    if num % 11 == 0 and num % 3 != 0:
        result.append(str(num))

# In kết quả, các số cách nhau bằng "; "
print("; ".join(result))
