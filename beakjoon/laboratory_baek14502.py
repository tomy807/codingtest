import sys
from collections import deque
from pprint import pprint
from itertools import combinations
import copy
N,M=map(int, sys.stdin.readline().split())
graph=[]
virus=[]
empty=[]
dx=[-1,0,0,1]
dy=[0,1,-1,0]
answer=[]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            virus.append((i,j))
        elif graph[i][j]==0:
            empty.append((i,j))
com=list(combinations(empty, 3))
queue=deque([])
for combi in com:
    count=0
    newgraph=copy.deepcopy(graph)
    for make1 in combi:
        newgraph[make1[0]][make1[1]]=1
    for i,j in virus:
        queue.append((i,j))
        while queue:
            out=queue.popleft()
            for k in range(4):
                ny=out[0]+dy[k]
                nx=out[1]+dx[k]
                if 0<=ny<N and 0<=nx<M and newgraph[ny][nx]==0:
                    queue.append((ny,nx))
                    newgraph[ny][nx]=2
    for i in range(N):
        for j in range(M):
            if newgraph[i][j]==0:
                count+=1
    answer.append(count)
print(max(answer))
