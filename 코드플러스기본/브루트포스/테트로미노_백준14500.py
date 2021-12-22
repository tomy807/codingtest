import sys

def dfs(x,y,depth,sumN):
    global maxSum
    if maxSum >= sumN + max_val * (3 - depth):
        return
    if depth==3:
        maxSum= max(maxSum,sumN)     
        return   
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N and visited[ny][nx]==0:
                if depth==1:
                    visited[ny][nx]=1
                    dfs(x, y, depth+1,sumN+board[ny][nx])
                    visited[ny][nx]=0
                visited[ny][nx]=1
                dfs(nx, ny, depth+1,sumN+board[ny][nx])
                visited[ny][nx]=0
                
N,M=map(int,sys.stdin.readline().split(' '))
board=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
maxSum=0
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split(' '))))
visited=[[0 for _ in range(M)] for _ in range(N)]
max_val=max(map(max,board))
for y in range(N):
    for x in range(M):
        visited[y][x]=1
        dfs(x, y, 0,board[y][x])
        visited[y][x]=0
print(maxSum)