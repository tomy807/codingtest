import sys

def dp(n):
    a=[0]*(n+1)
    a[0]=0
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    elif n==4:
        return 7
    else:
        a[1]=1
        a[2]=2
        a[3]=4
        a[4]=7
        for i in range(4,n+1):
            a[i]=a[i-1]+a[i-2]+a[i-3]
    return a[n]
T=int(sys.stdin.readline())
for _ in range(T):
    print(dp(int(sys.stdin.readline())))
