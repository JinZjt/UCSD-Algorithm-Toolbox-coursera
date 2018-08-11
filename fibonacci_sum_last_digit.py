# Uses python3
import sys
#import numpy as np
'''def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
'''
'''def calc_fib_fast(n):
   a=0
   b=1
   if n==0:
       sum =0
   else:
       sum=1
   for i in range(2,n+1):
       c = (a%10+b%10)%10
       sum+=c
       if sum >=10:
           sum = sum%10
       a = b
       b = c
   return sum
'''
#print(calc_fib_fast())
def fib_fast_sum_last(n):
    sum_, a, b = 0,0,1
    for i in range(n%60):
        sum_ = (sum_ + b) % 10
        a, b= b, (a+b)%10
    return sum_
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_fast_sum_last(n))

'''for j in range(100):
    p = np.random.randint(1,100)
    res1 = fibonacci_sum_naive(p)
    res2 = calc_fib_fast(p)
    if res1==res2:
        print("OK")
    else:
        print("wrong",p,res1,res2)
'''
'''
def fibonacci_last_digit_sum(n):
    sum_, a, b = 0, 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
        sum_ = (sum_ + b) % 10
    return a, b, sum_

seen = set()

for x in range(1000):
    triple = fibonacci_last_digit_sum(x)
    if triple in seen:
        print('Back to start:', x)
        break
    seen.add(triple)
'''