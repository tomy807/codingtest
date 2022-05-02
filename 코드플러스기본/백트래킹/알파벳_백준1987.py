import sys
from collections import deque
R,C=map(int, input().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited=[[0 for _ in range(C)] for _ in range(R)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs():
    maxint=1
    queue=set([(0,0,board[0][0])])
    while queue:
        x,y,path=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<C and 0<=ny<R and board[ny][nx] not in path:
                newpath=path+board[ny][nx]
                queue.add((nx,ny,newpath))
                maxint=max(maxint, len(newpath))
    return maxint
print(bfs())