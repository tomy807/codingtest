from collections import deque
N,M=map(int,input().split())
maze=[list(map(int, input())) for _ in range(M)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
wall_count=[[float('inf') for _ in range(N)] for _ in range(M)]
queue=set([(0,0,0)])
wall_count[0][0]=0
while(queue):
    x,y,walls=queue.pop()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            new_walls=walls
            if maze[ny][nx]==1:
                new_walls=walls+1
            if new_walls < wall_count[ny][nx]:
                    wall_count[ny][nx] = new_walls
                    queue.add((nx,ny,new_walls))
print(wall_count[M-1][N-1])