# Uses python3
import sys

def get_optimal_value(n,capacity, weights, values):
    max_value = 0
    valueList = []
    for i in range(n):
        valueList.append(values[i]/weights[i])
    
    mainList = zip(values,weights,valueList)
    mainList = list(mainList)
    mainList = sorted(mainList,key=lambda x:x[2],reverse=True)

    for i in mainList:
        if capacity!=0:
            if i[1]<=capacity:
                wt = i[1]
            elif i[1]>=capacity:
                wt = capacity
        
            max_value = max_value + (i[2]*wt)
            capacity = capacity - wt
        else:
            return max_value
    return max_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n,capacity, weights, values)
    print("{:.4f}".format(opt_value))
