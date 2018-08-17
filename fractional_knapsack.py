# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    order_ = []
    for i in range(len(weights)):
        ratio = values[i]/weights[i]
        tup = (ratio, weights[i])
        order_.append(tup)
    order_ = sorted(order_, reverse=True)
    for i in range(len(weights)):
        if capacity>=order_[i][1]:
            capacity -= order_[i][1]
            value += order_[i][0]*order_[i][1]
        elif capacity<order_[i][1] and capacity>0:
            value += capacity*order_[i][0]
            capacity =0
    return round(value,4)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

'''
a = [60,100,120]
b = [20,50,30]
print(get_optimal_value(40,b,a))
'''