# Uses python3
import sys
import random


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calcPisanoPeriod(number):
    previous = 0
    current = 1
    for i in range(0, number * number):
        previous, current = current, (previous+current) % number
        if(previous == 0 and current == 1):
            # print(i)
            return i+1


def fib(n, m):
    pisanaoPeriod = calcPisanoPeriod(m)
    # print(pisanaoPeriod)
    n = n % pisanaoPeriod
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        a, b = b, (a+b)
    return (b % m)


def calcSum(n):
    sums = 0
    for i in range(0, n+1):
        sums = sums + fib(i, 10)
    return (sums % 10)


if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(fib(n, m))
