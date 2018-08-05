# python3
import numpy as np

'''def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
'''
#-----------------------------------------------------------
#stress testing演示：第一种方法：直接排序，没有问题。第二种方法：遍历两遍，时间复杂度2n。在第二种方法里留了个破绽以显示stress testing的效果
def max_pairwise_product1(numbers):
    n=len(numbers)
    numsort = sorted(numbers)
    return (numsort[n-1])*(numsort[n-2])

def max_pairwise_product2(numbers):
    index1 = 0
    n = len(numbers)
    for i in range(1,n):
        if numbers[index1] < numbers[i]:
            index1 = i
    index2 = 0
    '''if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    '''
    for j in range(1,n):
        if (numbers[index2] < numbers[j]) and (j != index1):
            index2 = j
    return numbers[index1]*numbers[index2]
arr = np.arange(10)
for m in range(1000):
    np.random.shuffle(arr)
    a = max_pairwise_product1(arr)
    b = max_pairwise_product2(arr)
    if(a != b):
        print("wrong! The answer respectively are %d and %d" %(a,b),arr)
    else:
        print("OK!")

