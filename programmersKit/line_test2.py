from collections import deque
def solution(n, k):
    inf=n+1000
    answer = []
    visited=[]
    graph=[[inf for _ in range(n)] for _ in range(n)]
    visited.append((0,0))
    bfs(graph,visited)
    return answer
def bfs(graph,visited):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    for y,x in visited:
        graph[y][x]=0
    queue=deque(visited)
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and graph[ny][nx]>graph[y][x]+1:
                graph[ny][nx]=graph[y][x]+1