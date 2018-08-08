# Uses python3
'''def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

'''
import numpy as np
def calc_fib_fast(n):
   f = []
   f.append(0)
   f.append(1)
   for i in range(2,n+1):
       f.append(f[i-1] + f[i-2])
   return f[-1]

#stress testing__________________________________________________________
'''for i in range(100):
    p = np.random.randint(0,100)
    res1 = calc_fib_naive(p)
    res2 = calc_fib_fast(p)
    if res1 == res2:
        print("OK")
    else:
        print("wrong",p,res1,res2)
'''
n = int(input())
#print(calc_fib(n))
print(calc_fib_fast(n))
