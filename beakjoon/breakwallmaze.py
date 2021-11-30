import sys
from collections import deque

y_lenght, x_lenght=map(int,sys.stdin.readline().split())
maze=[]
answer=[]
for _ in range(y_lenght):
    li=list(sys.stdin.readline().strip())
    li1=list(map(int, li))
    maze.append(li1)
wallsInMaze=[(i,j) for i in range(y_lenght) for j in range(x_lenght) if maze[i][j]==1]

def bfs(maze):
    queue=deque()
    queue.append((0,0))
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    while queue:
        out=queue.popleft()
        for i in range(4):
            nexty=out[0]+dy[i]
            nextx=out[1]+dx[i]
            if 0<= nextx <x_lenght and 0<= nexty <y_lenght and maze[nexty][nextx]==0:
                maze[nexty][nextx]=maze[out[0]][out[1]]+1
                queue.append((nexty,nextx))
    return maze[y_lenght-1][x_lenght-1]

if x_lenght==1 and y_lenght==1:
    print(1)
else: 
    for wall in wallsInMaze:
        maze[wall[0]][wall[1]]=0
        road=bfs(maze)
        if road!=0:
            answer.append(road)
        maze[wall[0]][wall[1]]=1
    if answer:
        print(min(answer)+1)
    else:
        print(-1)