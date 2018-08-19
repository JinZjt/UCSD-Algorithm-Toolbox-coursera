# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x[-1])
    n = len(segments)
    i = 0
    while i<n:
        s = i+1
        points.append(segments[i][1])
        while i<n-1 and s<n and segments[i][1]>=segments[s][0] and segments[i][1]<=segments[s][1]:
            s +=1
        i = s
    points = list(set(points))
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

'''
a = [1, 3]
b = [2, 5]
c = [3, 6]
segments = [a,b,c]
'''
'''print(segments)
segments = sorted(segments, key = lambda x: x[-1])
print(segments)
print(len(segments))
points = []
for s in range(len(segments)):
    t = s+1
    while segments[s][1] >= segments[t][0] and segments[s][1] <= segments[t][1]:
        segments.remove(segments[t])
        points.append(segments[s][-1])
        if t==len(segments):
            break
    if t >= len(segments):
        break
points = list(set(points))
print(points)
'''
#print(optimal_points(segments))







