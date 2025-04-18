def addNum(a, b):
    '''
    Cho 2 số nguyên a, b được biểu diễn bởi 2 danh sách
    thực hiện phép cộng 2 số a, b trên 2 danh sách theo quy tắc cộng thông thường. kết quả trả về là 1 danh sách biểu diễn tổng a+b
    ví dụ 
    a = [1,2,4,5]
    b =   [7,8,9]

    c = [2,0,3,4]
    '''
    # Đảo ngược danh sách để bắt đầu từ hàng đơn vị
    a_rev = a[::-1]
    b_rev = b[::-1]

    # Đảm bảo hai danh sách có cùng độ dài bằng cách thêm số 0 vào ngắn hơn
    max_len = max(len(a_rev), len(b_rev))
    a_rev += [0] * (max_len - len(a_rev))
    b_rev += [0] * (max_len - len(b_rev))

    carry = 0  # Số nhớ
    result = []

    for digit_a, digit_b in zip(a_rev, b_rev):
        # Tính tổng từng cặp chữ số cùng với số nhớ
        total = digit_a + digit_b + carry
        # Chữ số tại vị trí hiện tại
        current_digit = total % 10
        # Số nhớ cho vị trí tiếp theo
        carry = total // 10
        result.append(current_digit)

    # Nếu còn số nhớ sau khi duyệt hết các chữ số
    if carry > 0:
        result.append(carry)

    # Đảo ngược kết quả để có thứ tự đúng và loại bỏ số 0 không cần thiết ở đầu (nếu có)
    c = result[::-1]
    # Loại bỏ các số 0 ở đầu (nếu có) nhưng giữ ít nhất 1 chữ số
    while len(c) > 1 and c[0] == 0:
        c = c[1:]

    return c
