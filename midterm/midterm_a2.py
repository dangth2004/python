import math


def projection_motion(v0, theta):
    """
    v0 và theta là hai giá trị đầu vào kiểu số thực cho bài toán ném xiên

    Thực hiện theo các yêu cầu CÂU 1 của đề bài
    """
    if v0 <= 0 or theta < 0 or theta > 90:
        print("ERROR")
    else:
        g = 9.81
        H = round((v0 ** 2 * math.sin(math.radians(theta)) ** 2) / (2 * g), 5)
        R = round((v0 ** 2 * math.sin(math.radians(2 * theta))) / g, 5)
        T = round((2 * v0 * math.sin(math.radians(theta))) / g, 5)
        return H, R, T


def caculate_time(t1, t2):
    """
    t1, t2 là hai tham số đầu vào có dạng chuỗi.

    Tính toán trả về khoảng thời gian theo yêu cầu CÂU 2 của đề bài.
    """
    return "hh:mm"
