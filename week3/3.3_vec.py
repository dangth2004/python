import math


def cosineb2v(u, v):
    # Kiểm tra hai vector cùng chiều dài
    if len(u) != len(v):
        raise ValueError("Hai vector phải có cùng số chiều")

    # Tính tích vô hướng (dot product)
    dot_product = sum(u_i * v_i for u_i, v_i in zip(u, v))

    # Tính độ dài (norm) của từng vector
    norm_u = math.sqrt(sum(u_i ** 2 for u_i in u))
    norm_v = math.sqrt(sum(v_i ** 2 for v_i in v))

    # Kiểm tra trường hợp vector 0
    if norm_u == 0 or norm_v == 0:
        raise ValueError("Vector không được có độ dài bằng 0")

    # Tính cosine của góc giữa hai vector
    cosine = dot_product / (norm_u * norm_v)

    return cosine
