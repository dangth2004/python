import math
from collections import Counter


def getTopWord(filename, n):
    """
    Hàm trả lại danh sách (list) n từ có số lần nhiều nhất trong file văn bản filename.
    Trong file văn bản filename, mỗi từ phân cách nhau bởi dấu cách
    Danh sách kết quả được sắp xếp giảm dần theo thứ tự từ điển của các từ.
    Nếu 2 từ có tần số xuất hiện bằng nhau thì ưu tiên từ có thứ tự từ điển lớn hơn
    (ví dụ 'd' > 'c' vì vậy nếu 'd' và 'c' có cùng số lần xuất hiện thì lấy 'd')
    Ví dụ, file văn bản có nội dung như sau:
    "
    a b c a a a b c d f d a d a f g s g h f s s a
    a g h b c e f g m n j s a r t y y u v z x k l a
    "

    danh sách các từ cùng số lần xuất hiện sắp xếp theo số lần xuất hiện giảm dần, từ giảm dần theo thứ tự từ điển như sau:

    [('a', 10), ('s', 4), ('g', 4), ('f', 4), ('d', 3), ('c', 3), ('b', 3), ('y', 2)
    , ('h', 2), ('z', 1), ('x', 1), ('v', 1), ('u', 1), ('t', 1), ('r', 1), ('n', 1)
    , ('m', 1), ('l', 1), ('k', 1), ('j', 1), ('e', 1)]

    Như vậy với n = 6, kết quả là

    ['s', 'g', 'f', 'd', 'c', 'a']


    Chú ý, file văn bản có nhiều dòng và không có ký tự unicode
    Nếu n > số từ thì kết quả là toàn bộ danh sách các từ.
    """
    with open(filename, 'r') as file:
        words = file.read().split()

    freq = Counter(words)

    # Sắp xếp: theo tần suất giảm dần, sau đó theo từ điển giảm dần
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], -ord(x[0][0])))
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]), reverse=True)

    return [word for word, count in sorted_words[:n]]


def getVector(filename, topword):
    """
        Hàm này trả lại danh sách (list) số nguyên tương ứng với vector biểu diễn văn bản trong file filename.
        phần tử thứ i trong danh sách là số lần từ topword[i] xuất hiện trong văn bản.

        ví dụ văn bản là
        "
        a b c a a a b c d f d a d a f g s g h f s s a
        a g h b c e f g m n j s a r t y y u v z x k l a
        "


        topword = ['s', 'g', 'f', 'd', 'a']

        kết quả là: [4, 4, 4, 3, 10]

    """
    with open(filename, 'r') as file:
        words = file.read().split()

    freq = Counter(words)
    return [freq[word] for word in topword]


def getCosineSim(u, v):
    """
        Phương thức tính cosine góc tạo bởi hai vector u, v

        cosine(u,v) = (u.v)/(||u||x||v||)

        ví dụ với u = [1,2,3,4], v = [1,2,1,1], kết quả làm tròn đến 5 chữ số là: 0.82808
    """
    dot = sum(ui * vi for ui, vi in zip(u, v))
    norm_u = math.sqrt(sum(ui ** 2 for ui in u))
    norm_v = math.sqrt(sum(vi ** 2 for vi in v))

    if norm_u == 0 or norm_v == 0:
        return 0.0  # để tránh chia cho 0

    cosine = dot / (norm_u * norm_v)
    return round(cosine, 5)


def sinhTaylor(x, e):
    """
     Viết chương trình tính sinh(x) theo khai triển Taylor,
     trong đó e là sai số để xác định  thời điểm dừng thuật toán,
     Thuật toán dừng lại tại số hạng Pi nếu |Pi - Pi-1| <= e

     ví dụ x = 5.5, e = 0.00001 kết quả làm tròn đến 5 chữ số là: 122.34392
          nhưng với e = 0.5     kết quả làm tròn đến 5 chữ số là: 122.34289

    """
    term = x  # số hạng đầu tiên (n = 0)
    sinh_val = term
    n = 1

    while True:
        prev_term = term
        term = term * (x ** 2) / ((2 * n) * (2 * n + 1))
        sinh_val += term
        if abs(term - prev_term) <= e:
            break
        n += 1

    return round(sinh_val, 5)


class Fraction:
    """
     Lớp thực hiện tạo đối tượng phân số cùng với các phép toán phân số,
     Tử số và mẫu số là số nguyên
     Các phép toán trên phân số gồm phép cộng, phép trừ, phép nhân, phép chia,
     Các phép toán này trả lại kết quả là một phân số ở dạng tối giản,
     ví dụ 2/3 + 7/3 thì kết quả là 3/1

    """

    def __init__(self, numerator, denominator):
        """
            Hàm dựng  của phân số gồm tử số numerator, và mẫu số denominator
            Chú ý tên của thuộc tính tử số và mẫu số đặt giống như trên (numerator và denominator)
        """
        if denominator == 0:
            raise ValueError("Mẫu số không được bằng 0.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify_self()

    def _simplify_self(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        # Đảm bảo mẫu số dương
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def addFraction(self, frac):
        """
            Hàm trả lại kết quả là phép cộng của phân số hiện tại với phân số frac
            ví dụ 2/3 + 7/3 thì kết quả là 3/1
        """
        num = self.numerator * frac.denominator + frac.numerator * self.denominator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def subFraction(self, frac):
        """
            Hàm trả lại kết quả là phép trừ của phân số hiện tại với phân số frac
            ví dụ 2/3 - 7/3 thì kết quả là -5/3
        """
        num = self.numerator * frac.denominator - frac.numerator * self.denominator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def multiFraction(self, frac):
        """
            Hàm trả lại kết quả là phép nhân của phân số hiện tại với phân số frac
            ví dụ 2/3 * 7/3 thì kết quả là 14/9
        """
        num = self.numerator * frac.numerator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def divFraction(self, frac):
        """
            Hàm trả lại kết quả là phép chia của phân số hiện tại với phân số frac
            ví dụ 2/3 : 7/3 thì kết quả là 2/7
        """
        if frac.numerator == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0.")
        num = self.numerator * frac.denominator
        den = self.denominator * frac.numerator
        return self.simplify(Fraction(num, den))

    def simplify(self, frac):
        """
            Hàm trả lại phân số tối giản của phân số frac
            ví dụ frac = 6/21 thì kết quả trả lại là 2/7
            thuật toán tìm phân số tối giản là chia cả tử số và mẫu số cho ước chung lớn nhất của tử số và mẫu số
        """
        gcd = math.gcd(frac.numerator, frac.denominator)
        num = frac.numerator // gcd
        den = frac.denominator // gcd
        if den < 0:
            num *= -1
            den *= -1
        return Fraction(num, den)

    def toString(self):
        """
            Hàm trả lại chuỗi biểu diễn phân số bởi tử số và mẫu số, ví dụ tử số  = 5, mẫu số = 7, kết quả trả lại chuỗi 5/7
            Hàm này đã được viết sẵn, sinh viên không chỉnh sửa.
        """
        return str(self.numerator) + '/' + str(self.denominator)


'''
    Chú ý, các phương thức sẽ được gọi đến để chấm điểm, 
    do vậy bài nộp của sinh viên cần phải bỏ hết (hoặc comment #) các lệnh in ra màn hình

'''
