import sys
def dp(stair,n):
    ans=[0 for _ in range(500)]
    for i in range(2):
        if i==0:
            ans[0]=max(ans[i-1]+stair[i],stair[i])
            continue
        ans[i]=max(ans[i-2]+stair[i],stair[i-1]+stair[i])
    for j in range(2,n):
        ans[j]=stair[j]+max(stair[j-1]+ans[j-3],ans[j-2])
    return ans[n-1]
if __name__=="__main__":
    stair=[0 for _ in range(500)]
    n=int(sys.stdin.readline())
    for i in range(n):
        stair[i]=int(sys.stdin.readline())
    print(dp(stair,n))
