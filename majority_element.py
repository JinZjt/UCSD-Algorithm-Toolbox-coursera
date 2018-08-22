# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #a是数组，left是左边元素，right是右边元素
    a = sorted(a)
    i = 1
    flag1 = 0
    flag2 = 0
    mark = []
    while i <= right-1:
        if a[i]!=a[i-1]:
            flag2 = i
            mark.append(flag2-flag1)
            flag1 = i
        if i==right-1 and a[i]==a[i-1]:
            mark.append(right-flag1)
        i+=1
    if max(mark) > right/2:
        return 1
    else:
        return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

'''
def majorelement(a,left,right):
    for i in range(left, right):
        currentelement = a[i]
        count = 0
        for j in range(left,right):
            if a[j]==currentelement:
                count +=1
        if count>(right/2):
            return 1
    return -1

a = [5,1,5,2,3,5]
print(get_majority_element(a,0,6))
print(majorelement(a,0,6))
'''