# Uses python3
import sys
import random
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
def gcd_fast(a, b):

    if b == 0:
        return a
    else:
        return gcd_fast(b,a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))
    # while(True):
    #     a = random.randint(1000,1000000)
    #     b = random.randint(1000,1000000)
    #     gcdNormal = gcd_naive(a,b)
    #     gcdfast = gcd_fast(a,b)
    #     if gcdNormal != gcdfast:
    #         print(a,b)
    #         print(gcdNormal)
    #         print(gcdfast)
    #         break
    #     else:
    #         print(a,b,"OK")