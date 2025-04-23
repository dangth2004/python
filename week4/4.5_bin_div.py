def binary_to_decimal(binary_str):
    """Chuyển số nhị phân (dạng chuỗi) sang số thập phân"""
    return int(binary_str, 2)


def is_divisible_by_5(binary_str):
    """Kiểm tra số nhị phân có chia hết cho 5 không"""
    decimal = binary_to_decimal(binary_str)
    return decimal % 5 == 0


# Nhập đầu vào
input_str = input()

# Tách các số nhị phân
binary_numbers = [num.strip() for num in input_str.split(',')]

# Lọc các số chia hết cho 5
result = [num for num in binary_numbers if len(num) == 4 and is_divisible_by_5(num)]

# In kết quả
print(','.join(result))
