# Uses python3
import sys
import random
def lcm_naive(a, b):
    
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def gcd_fast(a, b):

    if b == 0:
        return a
    else:
        return gcd_fast(b,a%b)
def lcm_fast(a,b):
    if a==0 and b==0:
        return 0
    return (abs(a*b)/gcd_fast(a,b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(lcm_fast(a, b)))
    # while(True):
    #     a = random.randint(100,10000)
    #     b = random.randint(100,10000)
    #     lcmnaive = lcm_naive(a,b)
    #     lcmfast = lcm_fast(a,b)
    #     if lcmnaive != lcmfast:
    #         print(a,b)
    #         print(lcmnaive)
    #         print(lcmfast)
    #         break
    #     else:
    #         print(a,b,"OK")
