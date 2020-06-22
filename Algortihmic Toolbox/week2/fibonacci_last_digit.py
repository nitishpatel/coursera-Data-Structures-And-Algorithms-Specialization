
def fibfast(n):

    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10
        return b
if __name__ == "__main__":
    n = int(input())
    fibAns = fibfast(n)
    # print(fibAns)
    print(fibAns)
    
