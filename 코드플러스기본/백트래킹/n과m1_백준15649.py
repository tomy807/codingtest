N,M=map(int, input().split())
visited=[0]*(N+1)
answer=[0]*(M+1)
def dfs(x):
    if x==M+1:
        for i in range(1,M+1):
            print(answer[i],end=' ')
        print()
    else:
        for i in range(1,N+1):
            if visited[i]==0:
                print(visited)
                print(answer)
                visited[i]=1
                answer[x]=i
                dfs(x+1)
                answer[x]=0
                visited[i]=0
dfs(1)