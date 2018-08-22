# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,3,4]
    minnumcoins = []
    minnumcoins.append(0)
    for value in range(1, m+1):
        minnumcoins.append(9999)
        for j in coins:
            if value>=j:
                numcoins = minnumcoins[value - j]+1
                if numcoins<minnumcoins[value]:
                    minnumcoins[value] = numcoins

    return minnumcoins[m]
#动态规划最重要的就在于记忆，比如说你想求第m项的值，你要依赖于前m-1项的结果。可能时间复杂度有些高，但是这么算出来结果准确。
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))



