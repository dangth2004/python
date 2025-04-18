def findUniq(a):
    '''
    Tìm phần tử xuất hiện đúng 1 lần trong danh sách.
    Sử dụng phép XOR để đạt độ phức tạp O(n) và không gian O(1)

    Ví dụ a = [1,2,3,2,3,1,4,5,4] phần tử cần tìm và trả về là 5
    '''
    result = 0
    for num in a:
        result ^= num
    return result
