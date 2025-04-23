a = input()

# Tạo các số aa, aaa, aaaa
aa = a * 2
aaa = a * 3
aaaa = a * 4

# Chuyển sang số nguyên
num_a = int(a)
num_aa = int(aa)
num_aaa = int(aaa)
num_aaaa = int(aaaa)

# Tính tổng
total = num_a + num_aa + num_aaa + num_aaaa

# In kết quả
print(f"{total}")
