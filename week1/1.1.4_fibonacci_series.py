# Hoàn thiện hàm fibonacciSeries(n) nhận vào số nguyên dương n và in ra n số đầu tiên của dãy Fibonacci.
def displayFibonacciSeries(n):
    if n <= 0:
        return
    fib_series = [1]  # F(0) = 1
    if n == 1:
        print(fib_series[0])
        return
    fib_series.append(1)  # F(1) = 1
    for i in range(2, n):
        next_num = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_num)
    print(' '.join(map(str, fib_series)))
