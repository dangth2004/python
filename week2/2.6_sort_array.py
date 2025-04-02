def inputArray():
    array = []
    # Nhập các số cách nhau bởi khoảng trắng từ bàn phím
    input_str = input("Nhập các phần tử của mảng, cách nhau bởi khoảng trắng: ")
    # Tách chuỗi thành các phần tử và chuyển sang số nguyên
    array = list(map(int, input_str.split()))
    return array


def sort_array(array):
    # Sắp xếp mảng theo thứ tự tăng dần
    r = sorted(array)
    return r


def printArray(r):
    # In các phần tử của mảng cách nhau bởi khoảng trắng
    print("Mảng sau khi sắp xếp:", ' '.join(map(str, r)))


# Chương trình chính
arr = inputArray()
r = sort_array(arr)
printArray(r)
