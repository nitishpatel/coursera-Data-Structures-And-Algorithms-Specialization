# Uses python3
import sys

def get_change(m):
    #write your code here
    dem = [10,5,1]
    count = 0
    while m > 0:
        for i in dem:
            if m - i >= 0:
                # print(i)
                count= count + 1
                m = m - i
                break
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
