# Nhập số nguyên dương từ bàn phím
n = int(input())

# Tạo dictionary với giá trị là đảo ngược của i*i
result = {}
for i in range(1, n + 1):
    squared = i * i
    reversed_squared = int(str(squared)[::-1])
    result[i] = reversed_squared

# In ra dictionary
print(result)
