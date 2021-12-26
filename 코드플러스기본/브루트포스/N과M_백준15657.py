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
            if depth==0 or out[-1]<=nums[i]:
                out.append(nums[i])
                dfs(N, M, depth+1)
                out.pop()
dfs(N, M, 0)