import sys
from collections import deque
M,N,H=map(int,sys.stdin.readline().split(' '))
tomatos=[]
tomatos1=[]
for _ in range(H):
    tomatos.append([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,-1,1]
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x]==1:
                tomatos1.append((z,y,x))
def bfs():
    queue=deque(tomatos1)
    while queue:
        z,y,x=queue.popleft()
        for i in range(6):
            nz=z+dz[i]
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M:
                if tomatos[nz][ny][nx]==0:
                    tomatos[nz][ny][nx]=tomatos[z][y][x]+1
                    queue.append((nz,ny,nx))
                
def result(M,N,H):
    maxn=0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatos[z][y][x]==0:
                    return -1
                maxn=max(maxn,tomatos[z][y][x])
    if max==1:
        return 0
    return maxn-1
bfs()
print(result(M,N,H))