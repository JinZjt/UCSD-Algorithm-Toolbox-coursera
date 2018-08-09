# Uses python3
import sys
#import numpy as np
'''def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
'''
def euclidean_gcd(a,b):
    if b==0:
        return a
    return euclidean_gcd(b,a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(euclidean_gcd(a, b))


#stress testing-----------------------------------------------------------------------------------------------
'''for i in range(100):
    a = np.random.randint(1, 10000)
    b = np.random.randint(1, 10000)
    res1 = gcd_naive(a,b)
    res2 = euclidean_gcd(a,b)
    if res1 == res2:
        print('OK')
    else:
        print("wrong", a,b,res1,res2)

'''