# -*- coding: utf-8 -*-
import locale

# Thiết lập locale cho tiếng Việt
locale.setlocale(locale.LC_ALL, 'vi_VN')


def inputList():
    names = []
    while True:
        line = input().strip()
        if line == "":
            break
        names.append(line)
    return names


def getName(s):
    # Tách họ đệm và tên
    parts = s.split()
    if not parts:
        return ('', '')

    # Tên là từ cuối cùng
    fname = parts[-1]

    # Họ đệm là tất cả các từ trước đó
    lname = ' '.join(parts[:-1]) if len(parts) > 1 else ''

    return (lname, fname)


def sortNamesList(names):
    # Tạo danh sách các tuple (họ đệm, tên, tên đầy đủ) để sắp xếp
    name_tuples = []
    for name in names:
        lname, fname = getName(name)
        name_tuples.append((lname, fname, name))

    # Sắp xếp theo tên (fname), nếu trùng thì sắp xếp theo họ đệm (lname)
    # Sử dụng locale.strxfrm để so sánh chuỗi tiếng Việt
    name_tuples.sort(key=lambda x: (locale.strxfrm(x[1]), locale.strxfrm(x[0])))

    # Trả về danh sách tên đã sắp xếp
    names_sorted = [item[2] for item in name_tuples]
    return names_sorted
