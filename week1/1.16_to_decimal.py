def convert(binary_str):
    binary_str = binary_str.strip().replace(" ", "")  # Loại bỏ khoảng trắng
    if not all(c in "01" for c in binary_str):  # Kiểm tra chuỗi hợp lệ
        raise ValueError("Chuỗi chỉ được chứa 0 và 1")

    decimal_value = 0
    length = len(binary_str)

    for i in range(length):
        bit = int(binary_str[i])  # Chuyển ký tự thành số (0 hoặc 1)
        power = length - 1 - i  # Tính lũy thừa của 2 theo vị trí
        decimal_value += bit * (2 ** power)  # Nhân giá trị bit với 2^power và cộng dồn

    return decimal_value
