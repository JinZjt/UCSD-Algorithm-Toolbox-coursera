 # Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    sum_ = 0
    i=1
    if n==2:
        summands.append(2)
        return summands
    while i>=0:
        sum_ += i
        if n-sum_ <= i:
            summands.append(n-sum(summands))
            break
        summands.append(i)
        i = i+1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

#print(optimal_summands(15))
