import numpy as np


def get_scores(ans, keys):
    """
    cho hai danh sách đầu vào ans và keys có kiểu dữ liệu string
    ans: một chuỗi các câu trả lời trắc nghiệm của sinh viên.
    keys: một chuỗi đáp án tương ứng với mỗi câu hỏi.

    Với mỗi câu trả lời đúng được tính 5 điểm, sai bị trừ 1 điểm.
    Hãy trả về số điểm của sinh viên.

    Với sinh viên không trả lời đủ 25 câu hỏi sẽ bị điểm liệt (0 điểm).

    Ví dụ:
    input:
    ans: CABABBCCCCBCACACACBCBAACC
    keys: ABCBBABCABCCAAAAABACABBAA
    output: 10

    ans: CABABBCCCCBCCACACBCBAACC
    keys: ABCBBABCABCCAAAAABACABBAA
    output: 0
    """
    if len(ans) != 25:
        return 0  # điểm liệt

    score = 0
    for a, k in zip(ans, keys):
        if a == k:
            score += 5
        else:
            score -= 1
    return score


def find_max_word(wordFreq):
    """
    Đầu vào là một từ điển có khóa là từ, giá trị là số lần xuất hiện của từ đó trong 1 doccument.
    Hãy trả về từ có số lần xuất hiện nhiều nhất trong từ điển

    Nếu có 2 từ cùng số lần xuất hiện nhiều nhất, trả ra từ lớn hơn theo thứ tự trong từ điển.

    Ví dụ:
    input: {'busy': 11, 'actor': 10, 'parent': 11, 'point': 11, 'slow': 10}
    output: point
    """
    max_freq = max(wordFreq.values())
    candidates = [word for word, freq in wordFreq.items() if freq == max_freq]
    return max(candidates)  # từ lớn hơn theo thứ tự từ điển


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(matrix):
    """
    matrix là một danh sách gồm n phần tử trong đó mỗi phần tử là một danh sách n số nguyên.
    Có thể hình dung matrix như một ma trận vuông có số chiều là (n, n).

    Hãy tìm và trả về theo thứ tự tăng dần về giá trị các số nguyên tố nằm trong
    MA TRẬN TAM GIÁC TRÊN của matrix

    Sinh viên có thể viết thêm các hàm phụ trợ nếu cần thiết.

    Ví dụ:
    input: [[9, 7, 18, 13],
            [29, 18, 1, 27],
            [24, 6, 14, 12],
            [2, 22, 25, 24]]
    output: [7, 13]
    """
    n = len(matrix)
    result = []
    for i in range(n):
        for j in range(i, n):  # chỉ lấy phần tam giác trên
            if is_prime(matrix[i][j]):
                result.append(matrix[i][j])
    return sorted(result)


def sort_three(arr):
    """
    arr là một danh sách các số nguyên. hãy sắp xếp các phần tử trong danh sách theo quy tắc sau:

    số chia hết cho 3 về cuối danh sách, sắp xếp theo thứ tự giảm dần
    Các số còn lại về đầu danh sách, giữ nguyên thứ tự xuất hiện như trong danh sách ban đầu

    Ví dụ:
    input: [1, 7, 6, 3, 3, 3, 2, 9, 2, 1]
    ouptut: [1, 7, 2, 2, 1, 9, 6, 3, 3, 3]
    """
    divisible_by_3 = sorted([x for x in arr if x % 3 == 0], reverse=True)
    not_divisible_by_3 = [x for x in arr if x % 3 != 0]
    return not_divisible_by_3 + divisible_by_3
