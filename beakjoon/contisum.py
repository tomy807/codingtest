import sys
def solve(n):
    ans=[]
    ans.append(dp[0])
    for i in range(1,n):
        dp[i]=max(dp[i-1]+li[i],li[i])
        ans.append(dp[i])
    return max(ans)
if __name__=="__main__":
    n=int(input())
    li=list(map(int,input().split()))
    dp=[0]*1001
    dp[0]=li[0]
    print(solve(n))

n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))