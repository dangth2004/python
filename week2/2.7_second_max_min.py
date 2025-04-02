def input_array():
    array = []
    input_str = input()
    array = list(map(int, input_str.split()))
    return array


def find_second_max_min(array):
    if len(array) < 2:
        return None, None  # Không đủ phần tử để tìm

    # Loại bỏ các phần tử trùng lặp và sắp xếp
    unique_sorted = sorted(set(array))

    if len(unique_sorted) == 1:
        return None, None  # Tất cả phần tử giống nhau

    # Tìm second_min và second_max
    second_min = unique_sorted[1] if len(unique_sorted) > 1 else None
    second_max = unique_sorted[-2] if len(unique_sorted) > 1 else None

    return second_min, second_max


array = input_array()
print(find_second_max_min(array))
