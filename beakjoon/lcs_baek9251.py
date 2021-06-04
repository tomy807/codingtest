import sys
def solve(p1,p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i]==p2[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
    return dp[len(p1)][len(p2)]

if __name__=="__main__":
    p1=input()
    p2=input()
    dp=[[0 for _ in range(len(p2)+1)] for _ in range(len(p1)+1)]
    print(solve(p1, p2))