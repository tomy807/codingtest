import sys

INF=100001
n=int(sys.stdin.readline())
lines=int(sys.stdin.readline())
graph=[[INF for _ in range(n+1)] for _ in range(n+1)]
for line in range(lines):
    a,b,w=map(int,sys.stdin.readline().split())
    graph[a][b]=min(w,graph[a][b])
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i!=j and graph[i][j]>graph[i][k]+graph[k][j]:
                 graph[i][j]=graph[i][k]+graph[k][j]
for line in graph[1:]:
    for i in line[1:]:
        if i==INF:
            print(0,end=' ')
        else:
            print(i,end=' ')
    print()