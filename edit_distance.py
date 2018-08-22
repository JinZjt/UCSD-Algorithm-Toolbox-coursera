# Uses python3
import numpy as np
def edit_distance(s, t):
    #write your code here
    length1 = len(s)
    length2 = len(t)
    Matrix = np.zeros((length1+1,length2+1))
    for i in range(1,length1+1):
        Matrix[i][0] = i
    for j in range(1, length2+1):
        Matrix[0][j] = j
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            insertion = Matrix[i][j-1]+1
            deletion = Matrix[i-1][j]+1
            mismatch = Matrix[i-1][j-1]+1
            match = Matrix[i-1][j-1]
            if s[i-1]==t[j-1]:
                Matrix[i][j] = min(insertion, deletion, match)
            else:
                Matrix[i][j] = min(insertion, deletion, mismatch)
    return (int)(Matrix[length1][length2])

if __name__ == "__main__":
    print(edit_distance(input(), input()))




