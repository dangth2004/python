# Nhập danh sách chuỗi từ bàn phím, cách nhau bởi dấu cách
inputs = input().split()

# Tạo từ điển với xâu đối xứng
result = {}
for s in inputs:
    result[s] = s + s[::-1]

# In từ điển
print(result)
