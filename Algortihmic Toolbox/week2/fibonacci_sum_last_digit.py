# Uses python3
import sys
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sums      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sums += current

    return sums % 10
# def calcPisanoPeriod(number):
#     previous = 0
#     current = 1
#     for i in range(0,number * number):
#         previous , current = current , (previous+current)%number
#         if(previous==0 and current ==1):
#             # print(i)
#             return i+1
def fib(n):
    if n <=1:
        return n
    n =(n+2)%60
    a,b = 0,1
    
    for i in range(2,n+1):
        a,b = b,(a+b)
    return ((b-1) % 10) 

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fib(n))
