N,M=map(int, input().split(' '))
graph=[[] for _ in range(N)]
visited=[False]*N
for _ in range(M):
    a,b=map(int,input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
def dfs(node,depth):
    if depth==4:
        print(1)
        exit()
        return
    for i in graph[node]:
        if not visited[i]:
            visited[i]=True
            dfs(i, depth+1)
            visited[i]=False
    
for start in range(N):
    visited[start]=True
    dfs(start,0)
    visited[start]=False
print(0)