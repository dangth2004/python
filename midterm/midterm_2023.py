import math


def find_minimum_sum(nums):
    """
    Tìm đỉnh núi có tổng nhỏ nhất.
    Cho một danh sách số nguyên dương nums
    Bộ 3 chỉ số i, j, k được gọi là đỉnh núi nếu thỏa mãn:
    i < j < k và nums[i] < nums[j] và nums[j] > nums[k]
    Ví dụ 1: input [8,6,1,5,3]
    với i = 2, j = 3 k = 4 tương ứng tạo thành một đỉnh núi với tổng bằng 9 (1 + 5 + 3)
    output: 9
    Ví dụ 2: input [5,4,8,7,10,2]
    i = 0, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 15.
    i = 1, j = 4, k = 5 tạo thành một đỉnh núi với tổng bằng 16.
    output : 13
    Nếu không tồn tại đỉnh núi nào trong danh sách
    output : -1
    """
    min_sum = float('inf')
    n = len(nums)
    found = False

    for j in range(1, n - 1):
        for i in range(0, j):
            if nums[i] < nums[j]:
                for k in range(j + 1, n):
                    if nums[k] < nums[j]:
                        found = True
                        total = nums[i] + nums[j] + nums[k]
                        if total < min_sum:
                            min_sum = total

    return min_sum if found else -1


def cosin_distance(v1, v2):
    """
    Tính khoảng cách cosin của 2 vector,
    input: v1, v2 là danh sách có cùng kích thước
    Cosin distance được tính theo công thức:
    cho trong đề bài.
    """
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))

    if norm1 == 0 or norm2 == 0:
        return -1  # hoặc raise Exception nếu cần thiết

    cosine_sim = dot / (norm1 * norm2)
    return round(cosine_sim, 3)


def get_hightest_gdp(country_list):
    """
    country_list là một danh sách trong đó mỗi phần tử là một tuple có cấu trúc như sau:
    (country_id, region, gdp, area)
    country_id: mã quốc gia
    region: khu vực (Asia, EU, USA...)
    gdp: tổng thu nhập quốc dân
    area: diện tích tương ứng với quốc gia đó
    tìm ra và trả về một danh sách 3 mã quốc gia
    có chỉ số gdp cao nhất được sắp xếp giảm dần theo chỉ số gdp.
    """
    # Sắp xếp theo gdp giảm dần
    sorted_list = sorted(country_list, key=lambda x: x[2], reverse=True)
    # Trả về 3 mã quốc gia đầu tiên
    return [item[0] for item in sorted_list[:3]]
