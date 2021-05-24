import sys
def fibonacci(n):
    dp0=[0]*41
    dp1=[0]*41
    dp0[0]=1
    dp0[1]=0
    dp1[0]=0
    dp1[1]=1
    if n==0:
        return dp0[0],dp1[0]
    if n==1:
        return dp0[1],dp1[1]
    for i in range(2,n+1):
        dp0[i]=dp0[i-1]+dp0[i-2]
        dp1[i]=dp1[i-1]+dp1[i-2]
    return dp0[i],dp1[i]
if __name__=="__main__":
    answer=[]
    test=int(sys.stdin.readline())
    for _ in range(test):
        n=int(sys.stdin.readline()) 
        answer.append(fibonacci(n))
    for i in answer:
        print(i[0],i[1])