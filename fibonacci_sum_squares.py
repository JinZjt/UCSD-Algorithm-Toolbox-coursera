 # Uses python3
from sys import stdin

'''def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
'''


def calc_fib_square_fast(n):
    sum_, a, b = 0,0,1
    for i in range(n%60):
        sum_ = b*(a+b)%10
        a, b = b, (a+b)%10
    return sum_

if __name__ == '__main__':
    n = int(stdin.read())
    print(calc_fib_square_fast(n))


'''def fib_test(n):
    sum_, a, b = 0,0,1
    for i in range(n):
        sum_ = b*(b+a)
        a, b = b, (a+b)%10
    return a, b, sum_
seen = set()
for x in range(1000):
    triple = fib_test(x)
    if triple in seen:
        print("back to start:", x)
        break
    seen.add(triple)
'''