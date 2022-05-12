import sys
from collections import deque
import copy
board=[list(sys.stdin.readline().rstrip()) for _ in range(8)]

def bfs():
    dx=[0,1,1,0,-1,-1,-1,0,1]
    dy=[0,0,1,1,1,0,-1,-1,-1]
    startx=0
    starty=7
    queue=deque([])
    queue.append((startx,starty))
    depth=0
    while queue:
        for _ in range(len(queue)):
            nowx,nowy=queue.popleft()
            print(nowx,nowy)
            if nowx==7 and nowy==0:
                return 1
            elif board[nowy][nowx]=='#':
                continue
            for i in range(9):
                nextx=nowx+dx[i]
                nexty=nowy+dy[i]
                if 0<=nextx<8 and 0<=nexty<8:
                    if board[nexty][nextx]=='#':
                        continue
                    queue.append((nextx,nexty))
        board.pop()
        board.insert(0,['.', '.', '.', '.', '.', '.', '.', '.'])
        depth+=1
        if depth==9:
            return 1
    return 0
print(bfs())
