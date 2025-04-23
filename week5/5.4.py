def findCouple(filename):
    """Tìm và trả về cặp đôi hoàn hảo trong file văn bản"""
    words = []

    # Đọc tất cả các từ từ file vào danh sách
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words.extend(line.split())

    # Tạo một set để kiểm tra nhanh
    word_set = set(words)

    # Tìm cặp đôi hoàn hảo
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in word_set and word != reversed_word:
            # Trả về theo thứ tự tăng dần
            return tuple(sorted((word, reversed_word)))

    return ('None', 'None')  # Trả về nếu không tìm thấy
