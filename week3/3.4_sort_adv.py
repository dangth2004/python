# Hoàn thiện hàm customSort


def customSort(a):
    '''
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    '''
    # Tách chẵn và lẻ
    evens = [x for x in a if x % 2 == 0]
    odds = [x for x in a if x % 2 != 0]

    # Sắp xếp chẵn tăng dần, lẻ giảm dần
    evens_sorted = sorted(evens)
    odds_sorted = sorted(odds, reverse=True)

    # Kết hợp kết quả
    return evens_sorted + odds_sorted
