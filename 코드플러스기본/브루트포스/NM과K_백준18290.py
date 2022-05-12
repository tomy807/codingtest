N,M,K=map(int, input().split(' '))
board=[]
visited=[[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,depth,sumN):
    if depth==K:
        return
    else:
        return