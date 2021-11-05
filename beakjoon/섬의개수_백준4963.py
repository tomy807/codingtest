import sys
from collections import deque
def bfs(graph,lands,w,h):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[1,0,-1,1,-1,1,0,-1]
    count=0
    visited=[]
    queue=deque([])
    for land in lands:
        if land in visited:
            continue
        count+=1
        queue.append(land)
        while(queue):
            out=queue.popleft()
            for i in range(8):
                ny=out[0]+dy[i]
                nx=out[1]+dx[i]
                if 0<=ny<h and 0<=nx<w and graph[ny][nx]==1 and (ny,nx) not in visited:
                    visited.append((ny,nx))
                    queue.append((ny,nx))
    return count

if __name__ == '__main__':
    while (True):
        graph=[]
        lands=[]
        w,h=map(int,sys.stdin.readline().split())
        if w==0 and h==0:
            break
        for _ in range(h):
            graph.append(list(map(int,sys.stdin.readline().split())))
        for i in range(h):
            for j in range(w):
                if graph[i][j]==1:
                    lands.append((i,j))
        print(bfs(graph,lands,w,h))
        