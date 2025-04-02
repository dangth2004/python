def convert(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  # Lấy phần dư và thêm vào trước chuỗi kết quả
        n //= 2  # Chia n cho 2

    return binary
