# Uses python3
import sys

def calc_fib_fast(n):
   f = []
   f.append(0)
   f.append(1)
   for i in range(2,n+1):
       f.append((f[i-1]%10+f[i-2]%10))
   return f[-1]%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calc_fib_fast(n))
