import math


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


def testDemo():
    a = Fraction(2, 3)
    b = Fraction(7, 3)

    print(a.addFraction(b).toString())
    print(a.subFraction(b).toString())
    print(a.multiFraction(b).toString())
    print(a.divFraction(b).toString())


'''
Bỏ comment lệnh testDemo() dưới đây để chạy chương trình, và comment lại lệnh đó khi nộp bài
'''
# testDemo()
