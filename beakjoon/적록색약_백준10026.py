import sys
from collections import deque
import pprint
N=int(sys.stdin.readline())
map=[list(sys.stdin.readline().strip()) for _ in range(N)]
visited=[[False for _ in range(N)] for _ in range(N)]
global count
count=0
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    global count
    count+=1
    queue=deque([(y,x)])
    color=map[y][x]
    print(color)
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if (0<=ny<N) and (0<=nx<N):
                if visited[ny][nx]==False and (map[y][x]==map[ny][nx]):
                    queue.append((ny,nx))
                    visited[ny][nx]=True
        pprint.pprint(visited)
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            bfs(i,j)
print(count)