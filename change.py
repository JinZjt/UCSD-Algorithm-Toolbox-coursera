# Uses python3
import sys

def get_change(m):
    count = [0,0,0]
    moneykind = [10,5,1]
    if m==0:
        return sum(count)
    for i in range(0,3):
        while m >= moneykind[i]:
            m-=moneykind[i]
            count[i]+=1
    return sum(count)
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
