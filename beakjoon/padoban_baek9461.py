import sys
dp=[0]*101
dp[1]=1
dp[2]=1
def padovan(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        for i in range(3,n+1):
            dp[i]=dp[i-2]+dp[i-3]
        return dp[n]
if __name__=="__main__":
    task=int(sys.stdin.readline())
    answer=[]
    for _ in range(task):
        n=int(sys.stdin.readline())
        answer.append(n)
    for i in answer:
        print(padovan(i))
        
