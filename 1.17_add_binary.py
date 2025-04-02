def add(a, b):
    a = a.strip()  # Remove any leading or trailing whitespace
    b = b.strip()

    max_len = max(len(a), len(b))  # Xác định độ dài lớn nhất
    a = a.zfill(max_len)  # Thêm số 0 vào đầu để hai chuỗi có cùng độ dài
    b = b.zfill(max_len)

    result = ""
    carry = 0  # Biến nhớ

    for i in range(max_len - 1, -1, -1):  # Duyệt từ phải sang trái
        bit_a = int(a[i])
        bit_b = int(b[i])

        sum_bits = bit_a + bit_b + carry  # Tổng của 2 bit + bit nhớ
        result = str(sum_bits % 2) + result  # Lưu kết quả bit
        carry = sum_bits // 2  # Tính bit nhớ

    if carry:  # Nếu còn bit nhớ cuối cùng, thêm vào kết quả
        result = "1" + result

    return result
