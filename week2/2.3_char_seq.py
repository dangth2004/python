S = input().strip()

# Đếm tần suất xuất hiện của từng ký tự
frequency = {}
for char in S:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Tìm ký tự có tần suất cao nhất
max_char = None
max_count = 0
for char, count in frequency.items():
    if count > max_count:
        max_char = char
        max_count = count

# In kết quả
print(f"{max_char} {max_count}")
