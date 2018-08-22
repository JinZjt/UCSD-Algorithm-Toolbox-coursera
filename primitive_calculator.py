# Uses python3
import sys

def real_optimal_sequence(n):
    seq = [[1],[1]]
    for i in range(2,n+1):
        res1,res2,res3 = 9999,9999,9999
        temp = []
        if i%2==0:
            res2 = len(seq[i//2])-1
        if i%3==0:
            res3 = len(seq[i//3])-1
        res1 = len(seq[i-1])-1
        if res3 ==min(res1, res2, res3):
            temp = seq[i//3].copy()
            temp.append(i)
            seq.append(temp)
        elif res2 == min(res1,res2,res3):
            temp = seq[i//2].copy()
            temp.append(i)
            seq.append(temp)
        elif res1 == min(res1, res2, res3):
            temp = seq[i-1].copy()
            temp.append(i)
            seq.append(temp)
    return seq[n]

#print(real_optimal_sequence(757))

'''
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
'''

input = sys.stdin.read()
n = int(input)
sequence = real_optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

#print(list(optimal_sequence(5)))
#print(real_optimal_sequence(1))
'''b = (1,2)
a = [[1],[1,2],[1,3]]
t = a[2].copy()
t.append(4)
a.append(t)
print(a)
'''
'''
def optimal_sequence(n):
    # Create a list which stores the hop count from an element to 1.
    hop_count = [0] * (n + 1)

    # Path from 1 to 1 is 1.
    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_count[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_count[i] = min_hops + 1

    # ptr points to current position of hop_count.
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        # The list contains next hop candidates.
        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        # Choose from the candidates whose hop count is the least.
        ptr = min(
            [(c, hop_count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)
print(list(optimal_sequence(757)))
'''
'''import numpy as np
for i in range(1000):
    n = np.random.randint(1,1000)
    res1 = real_optimal_sequence(n)
    res2 = list(optimal_sequence(n))
    length1 = len(res1)
    length2 = len(res2)
    if length1!=length2:
        print("wrong", length1,length2,n)
    else:
        print("ok!")
'''






