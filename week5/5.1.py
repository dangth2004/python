import os

def searchInFiles(x, path):
    result = []

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        # Kiểm tra xem có phải là file không
        if os.path.isfile(full_path):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if x in line:
                            # Giữ nguyên dòng có \n, và thêm đường dẫn vào tên file
                            result.append((os.path.join(path, filename), line))
                            break
            except:
                # Nếu không mở được file (ví dụ không phải file văn bản), bỏ qua
                continue

    # Sắp xếp kết quả theo tên file
    result.sort(key=lambda item: item[0])
    return result
