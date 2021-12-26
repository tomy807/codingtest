N,M= map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
nums.sort()
out=[]
visited=[False]*N
def dfs(N,M,depth):
    if depth==M:
        print(' '.join(map(str,out)))
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i]=True
                out.append(nums[i])
                dfs(N, M, depth+1)
                out.pop()  
                visited[i]=False
dfs(N, M, 0)