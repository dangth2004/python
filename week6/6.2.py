import math
from collections import defaultdict


def getTopWord(filename, n):
    word_count = defaultdict(int)

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_count[word] += 1

    # Sắp xếp theo số lần xuất hiện giảm dần, từ điển giảm dần
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], -ord(item[0][0]) if item[0] else (0, 0)))

    # Lấy n từ đầu tiên (chỉ lấy từ, không lấy số đếm)
    result = [word for word, count in sorted_words[:n]]

    return result


def getVector(filename, topword):
    word_count = defaultdict(int)

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in topword:
                    word_count[word] += 1

    # Tạo vector theo thứ tự topword
    vector = [word_count[word] for word in topword]
    return vector


def getCosineSim(u, v):
    if len(u) != len(v):
        return 0.0

    dot_product = sum(ui * vi for ui, vi in zip(u, v))
    norm_u = math.sqrt(sum(ui ** 2 for ui in u))
    norm_v = math.sqrt(sum(vi ** 2 for vi in v))

    if norm_u == 0 or norm_v == 0:
        return 0.0

    cosine_sim = dot_product / (norm_u * norm_v)
    return round(cosine_sim, 5)


def sinhTaylor(x, e):
    result = 0.0
    prev_term = 0.0
    n = 0

    while True:
        # Tính số hạng hiện tại: x^(2n+1) / (2n+1)!
        term = (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term

        # Kiểm tra điều kiện dừng
        if n > 0 and abs(term - prev_term) <= e:
            break

        prev_term = term
        n += 1

    return round(result, 5)


def testDemo():
    print(getTopWord('text.txt', 5))
    print(getVector('text.txt', getTopWord('text.txt', 5)))
    print(round(getCosineSim([1, 2, 3, 4], [1, 2, 1, 1]), 5))
    print(round(sinhTaylor(5.5, 0.5), 5))

# Bỏ comment để test, comment lại khi nộp bài
# testDemo()
