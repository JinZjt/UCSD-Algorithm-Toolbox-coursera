# Uses python3
import sys
import numpy as np
np.set_printoptions(suppress=True)
'''def lcm_naive(a, b):
    m = max(a,b)
    for l in range(m, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
'''
def euclidean_gcd(a,b):
    if b==0:
        return a
    return euclidean_gcd(b,a%b)
def lcm_fast(a,b):
    res = euclidean_gcd(a,b)
    return (a*b//res)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
