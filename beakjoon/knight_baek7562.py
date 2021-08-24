import sys
from collections import deque

def bfs(start,end,chess_size):
    chess_board=[[0 for _ in range(chess_size)] for _ in range(chess_size)]
    queue=deque()
    queue.append(start)
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    while queue:
        out=queue.popleft()
        nowx=out[1]
        nowy=out[0]
        for i in range(8):
            nexty=nowy+dy[i]
            nextx=nowx+dx[i]
            if 0<= nextx <chess_size and 0<= nexty <chess_size and chess_board[nexty][nextx]==0:
                chess_board[nexty][nextx]=chess_board[nowy][nowx]+1
                queue.append([nexty,nextx])
        if out==end:
            return chess_board[end[0]][end[1]]

answer=[]
test_case=int(sys.stdin.readline())
for _ in range(test_case):
    chess_size=int(sys.stdin.readline())
    start=list(map(int,sys.stdin.readline().split()))
    end=list(map(int,sys.stdin.readline().split()))
    if start[0]==end[0] and start[1]==end[1]:
        answer.append(0)
    else:
        answer.append(bfs(start,end,chess_size))
for i in answer:
    print(i)