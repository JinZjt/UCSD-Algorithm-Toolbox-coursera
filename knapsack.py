# Uses python3
import sys
import numpy as np

def real_optimal_weight(W, n, w):
    matrix = np.zeros((n+1, W+1))
    for i in range(1,n+1):
        for j in range(1,W+1):
            matrix[i][j] = matrix[i-1][j]
            if w[i-1]<=j:
                temp = w[i-1]
                weight = matrix[i-1][j-temp] + temp*1
                if weight>matrix[i][j]:
                    matrix[i][j] = weight
    return (int)(matrix[n][W])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(real_optimal_weight(W, n, w))










