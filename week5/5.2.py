def zeroMove(fileName):
    # Đọc nội dung file
    with open(fileName, 'r') as file:
        line = file.readline().strip()

    # Chuyển các số từ chuỗi sang danh sách số nguyên
    numbers = list(map(int, line.split()))

    # Tách các số khác 0 và các số 0
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]

    # Kết hợp lại với các số 0 ở cuối
    result = non_zeros + zeros

    return result
