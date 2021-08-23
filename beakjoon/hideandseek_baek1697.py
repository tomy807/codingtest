import sys
from collections import deque
MAX=100000
subinPoint,sisterPoint = map(int, sys.stdin.readline().split())
points= [0]*(MAX+1)

def bfs():
    queue=deque()
    queue.append(subinPoint)
    points[subinPoint]=1
    while queue:
        out= queue.popleft()
        if out==sisterPoint:
            return points[sisterPoint]
        for nextOut in (out-1,out+1,out*2):
            if 0<=nextOut<=MAX and points[nextOut]==0:
                queue.append(nextOut)
                points[nextOut]=points[out]+1        
print(bfs()-1)

