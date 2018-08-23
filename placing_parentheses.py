 # Uses python3
import numpy as np
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minandmax(i,j,dataset,M,m):
    Min = 999999
    Max = -999999
    for k in range(i,j):
        a = evalt(M[i,k], M[k+1,j],dataset[2*k-1])
        b= evalt(M[i, k], m[k + 1, j], dataset[2 * k - 1])
        c = evalt(m[i, k], M[k + 1, j], dataset[2 * k - 1])
        d = evalt(m[i, k], M[k + 1, j], dataset[2 * k - 1])
        Min = min(Min,a,b,c,d)
        Max = max(Max,a,b,c,d)
    return Min, Max
def get_maximum_value(dataset):
    n = (int)((len(dataset)+1)/2)
    M = np.zeros((n+1,n+1))
    m = np.zeros((n+1,n+1))
    for i in range(1,n+1):
        temp = (int)((i-1)*2)
        M[i][i] = dataset[temp]
        m[i][i] = dataset[temp]
    for s in range(1,n):
        for i in range(1,n-s+1):
            j = i+s
            m[i,j], M[i,j] = minandmax(i,j,dataset,M,m)
    return (int)(M[1,n])


if __name__ == "__main__":
    print(get_maximum_value(input()))
#a = [5,'-',8,'+',7,'*',4,'-',8,'+',9]
#print(get_maximum_value(a))