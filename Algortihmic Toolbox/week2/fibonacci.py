# Uses python3
def calc_fib(n):
    if n==0 or n==1:
        return n
    fibList=[0]*(n+1)
    # print(fibList)
    fibList[0]=0
    fibList[1]=1
    for i in range(2,n+1):
        fibList[i]=fibList[i-1]+fibList[i-2]
    return fibList[n]
if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
    
