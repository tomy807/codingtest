from collections import deque

N=int(input())
r1,c1,r2,c2=map(int, input().split())
board=[[0 for _ in range(N)] for _ in range(N)]
def bfs():
    dx=[-2,-2,0,0,2,2]
    dy=[-1,1,-2,2,-1,1]
    queue=deque([(r1,c1)])
    while queue:
        out=queue.popleft()
        x=out[0]
        y=out[1]
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[ny][nx]==0:
                    queue.append((nx,ny))
                    board[ny][nx]=board[y][x]+1
bfs()
if board[c2][r2]!=0:
    print(board[c2][r2])
else:
    print(-1)