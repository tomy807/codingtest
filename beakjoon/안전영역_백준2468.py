import sys
from collections import deque

def bfs(graph,rain,N):
    count=0
    visited=[[False for _ in range(N)] for _ in range(N)]
    dy=[-1,0,0,1]
    dx=[0,-1,1,0]
    queue=deque([])
    for i in range(N):
        for j in range(N):
            if visited[i][j] or graph[i][j]<=rain:
                continue
            count+=1
            visited[i][j]=True
            queue.append((i,j))
            while queue:
                out=queue.popleft()
                for k in range(4):
                    ny=out[0]+dy[k]
                    nx=out[1]+dx[k]
                    if 0<=ny<N and 0<=nx<N and graph[ny][nx]>rain and not visited[ny][nx]:
                        visited[ny][nx]=True
                        queue.append((ny,nx))
    return count

if __name__ == '__main__':
    N=int(sys.stdin.readline())
    graph=[]
    answer=[]
    height=0
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for line in graph:
        height=max(height,max(line))
    for rain in range(height):
        answer.append(bfs(graph,rain,N))       
    print(max(answer))