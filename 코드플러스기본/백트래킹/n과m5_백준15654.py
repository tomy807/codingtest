N,M= map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
visited=[0]*N
answer=[]
def dfs(depth):
    if depth==M:
        for i in answer:
            print(i,end=' ')
        print()
    else:
        for i in range(N):
            if visited[i]==0:
                visited[i]=1
                answer.append(nums[i])
                dfs(depth+1)
                answer.pop()
                visited[i]=0
dfs(0)