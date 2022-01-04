import sys
from collections import deque
S=int(input())
graph=[[0 for _ in range(1001)] for _ in range(1001)]

def bfs():
    screen=1
    clipBoard=0
    queue=deque([(screen,clipBoard)])
    while queue:
        screen,clipBoard=queue.popleft()
        if screen==S:
            return
        for nextStep in [(screen,screen),(screen+clipBoard,clipBoard),(screen-1,clipBoard)]:
            next_screen=nextStep[0]
            next_clipBoard=nextStep[1]
            if 0<=next_screen<1001 and 0<=next_clipBoard<1001 and graph[next_screen][next_clipBoard]==0 :
                graph[next_screen][next_clipBoard]=graph[screen][clipBoard]+1
                queue.append((next_screen,next_clipBoard))

bfs()
answer=sys.maxsize
for i in range(1001):
    if graph[S][i]!=0 and graph[S][i]<answer:
        answer=graph[S][i]
print(answer)