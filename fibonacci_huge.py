# Uses python3
import sys

'''def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
'''
def get_period_fast(m):
    f = []
    f.append(0)
    f.append(1)
    f.append(1)
    i = 2
    while True:
        i=i+1
        f.append(f[i-1]+f[i-2])
        if f[i]%m == 1 and f[i-1]%m == 1 and f[i-2]%m == 0:
            return i-2
def calc_fib_fast(n,m):
    f = [0,1]
    if n<=1:
        return f[n]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[-1]%m
#lenth = get_period_fast(239)
#rep = 2816213588%lenth
#print(calc_fib_fast(rep,239))
def get_fib_huge_fast(n,m):
    length = get_period_fast(m)
    replacement = n%length
    return calc_fib_fast(replacement ,m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fib_huge_fast(n,m))
