T=int(input())
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7
for i in range(5,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
for _ in range(T):
    print(dp[int(input())])
# 재귀
T=int(input())
def dfs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return dfs(n-1)+dfs(n-2)+dfs(n-3)
for _ in range(T):
    print(dfs(int(input())))
