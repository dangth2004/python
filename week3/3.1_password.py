def checkPassword(s):
    # Kiểm tra độ dài mật khẩu (8-100 ký tự)
    if len(s) < 8 or len(s) > 100:
        return False

    # Các cờ kiểm tra
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = {'~', '!', '@', '#', '$', '%', '^', '&', '*'}

    for char in s:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Kiểm tra tất cả điều kiện
    return has_upper and has_lower and has_digit and has_special
