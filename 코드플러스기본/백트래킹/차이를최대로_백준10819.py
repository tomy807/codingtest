N=int(input())
A=list(map(int, input().split()))
global answer
answer=0
visited=[0]*N
def dfs(depth,sums,lastNum):
    global answer
    if depth==N:
        answer=max(answer, sums)
        return
    else:
        for i in range(N):
            if visited[i]==0:
                visited[i]=1
                newSums=abs(lastNum-A[i])
                dfs(depth+1,sums+newSums,A[i])
                visited[i]=0
for i in range(N):
    visited[i]=1
    dfs(1, 0, A[i])
    visited[i]=0
print(answer)