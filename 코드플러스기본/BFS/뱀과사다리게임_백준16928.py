import sys
from collections import deque
N=int(input())
M=int(input())

ladder=dict()
snake=dict()
for _ in range(N):
    x,y=map(int, sys.stdin.readline())
    ladder[x]=y
for _ in range(M):
    u,v=map(int,sys.stdin.readline())
    snake[v]=u

visited=[False]*101
board_cnt=[0]*101

def bfs():
    queue=deque([1])
    while(queue):
        now=queue.popleft()
        for move in range(1,7):
            check_move=now+move
            