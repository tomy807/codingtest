import sys
from collections import deque

x_lenght, y_lenght=map(int,sys.stdin.readline().split())
ground=[]
for _ in range(y_lenght):
    ground.append(list(map(int,sys.stdin.readline().split())))
exist1InGround=[(i,j) for i in range(y_lenght) for j in range(x_lenght) if ground[i][j]==1]


def bfs(exist1InGround):
    queue=deque(exist1InGround)
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    while queue:
        out=queue.popleft()
        for i in range(4):
            nextx= out[1]+dx[i]
            nexty= out[0]+dy[i]
            if 0<= nextx <x_lenght and 0<= nexty <y_lenght and ground[nexty][nextx]==0:
                ground[nexty][nextx]=ground[out[0]][out[1]]+1
                queue.append((nexty,nextx))
bfs(exist1InGround)
compare=-2
isTrue=False
for k in ground:
    for tomato in k:
        if tomato==0:
            isTrue=True
        else:
            compare=max(tomato,compare)
if isTrue:
    print(-1)
else:
    print(compare-1)