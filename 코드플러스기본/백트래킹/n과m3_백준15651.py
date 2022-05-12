N,M=map(int, input().split())
answer=[0]*M
def dfs(depth):
    if depth==M:
        for i in answer:
            print(i,end=' ')
        print()
    else:
        for i in range(1,N+1):
            answer[depth]=i
            dfs(depth+1)
dfs(0)