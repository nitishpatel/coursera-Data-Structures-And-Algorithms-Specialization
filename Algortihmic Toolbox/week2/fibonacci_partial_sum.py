# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10
# def calcPisanoPeriod(number):
#     previous = 0
#     current = 1
#     for i in range(0, number * number):
#         previous, current = current, (previous+current) % number
#         if(previous == 0 and current == 1):
#             # print(i)
#             return i+1


def fib(n, m=10):
    if n<=1:
        return n
    pisanaoPeriod = 60
    # print(pisanaoPeriod)
    n = n % pisanaoPeriod
    a, b = 0, 1
    
    for i in range(2,n+1):
        a, b = b, (a+b)
    return (b % m)

def fibonacci_partial_sum_improved(m, n):
    return (fib(n+2, 10) + 10 - fib(m+1, 10)) % 10
if __name__ == '__main__':
    
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_improved(from_,to))
