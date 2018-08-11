# Uses python3
import sys

'''def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10
'''
fib_list = [0,1]
for i in range(2,60):
    fib_list.append(fib_list[i-1]%10+fib_list[i-2]%10)
def fib_part_sum_fast(from_, to):
    from_ = from_%60
    to = to%60
    if from_ > to:
        to = to+60
    sum_ = 0
    for i in range(from_, to+1):
        sum_ = sum_ + fib_list[i%60]
    return sum_%10

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fib_part_sum_fast(from_, to))
