import sys
from collections import deque
def bfs():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append((0,0))
    while queue:
        out=queue.popleft()
        for i in range(4):
            nx=out[0]+dx[i]
            ny=out[1]+dy[i]
            if 0<= nx <x and 0<= ny <y and maze[nx][ny]==1:
                queue.append((nx,ny))
                maze[nx][ny]=maze[out[0]][out[1]]+1
    print(maze[x-1][y-1])
if __name__=="__main__":
    x,y=map(int,sys.stdin.readline().split())
    maze=[]
    for _ in range(x):
        line=list(map(int,list(sys.stdin.readline().strip())))
        maze.append(line) 
    bfs()
