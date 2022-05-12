import sys
from collections import deque
W,H=map(int,input().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(H)]
cntBoard=[[0 for _ in range(W)] for _ in range(H)]
pointC=[]
for i in range(H):
    for j in range(W):
        if(board[i][j]=='C'):
            pointC.append((i,j))

def bfs():
    queue=deque([])