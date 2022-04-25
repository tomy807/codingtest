import sys
from collections import deque
N,M= map(int,sys.stdin.readline().split())
ladder={floor:0 for floor in range(101)}
visited = [False] * 101
board_cnt = [0] * 101
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    ladder[x]=y
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    ladder[u]=v
def bfs():
    queue=deque([])
    queue.append(1)
    visited[1] = True
    while queue:
        now = queue.popleft()
        for move in range(1,7):
            check_move = now+move
            if 0 < check_move <= 100 and not visited[check_move]:
                if ladder[check_move]!=0:
                    check_move = ladder[check_move]

                if not visited[check_move]:
                    queue.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] = board_cnt[now] + 1

bfs()
print(board_cnt[100])