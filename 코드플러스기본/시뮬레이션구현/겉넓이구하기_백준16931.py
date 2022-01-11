N,M=map(int, input().split(' '))
graph=[list(map(int, input().split())) for _ in range(N)]
cnt=N*M
for i in range(N):
    cnt+=graph[i][0]
    for j in range(1,M):
        if graph[i][j]>graph[i][j-1]:
            cnt+=(graph[i][j]-graph[i][j-1])
for i in range(M):
    cnt+=graph[0][i]
    for j in range(1,N):
        if graph[i][j]>graph[i-1][j]:
            cnt+=(graph[i][j]-graph[i-1][j])
print(cnt*2)