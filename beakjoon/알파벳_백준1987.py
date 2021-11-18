import sys
from collections import deque
R,C=map(int,sys.stdin.readline().split(' '))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
map=[list(sys.stdin.readline().strip()) for _ in range(R)]

def bfs(R,C):
    maxlenght=1
    queue=set([(0,0,map[0][0])])
    while queue:
        y,x,line=queue.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<R and 0<=nx<C and map[ny][nx] not in line:
                newline=line+map[ny][nx]
                queue.add((ny,nx,newline))
                maxlenght=max(len(newline),maxlenght)
    return maxlenght
print(bfs(R, C))


