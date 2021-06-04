import sys

def solve(n):
    ans=dp[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+li[i],li[i])
        ans=max(ans,dp[i])
    return ans
if __name__=="__main__":
    n=int(input())
    li=list(map(int,input().split()))
    dp=[0]*100001
    dp[0]=li[0]
    print(solve(n))