import sys
from collections import deque,defaultdict
nodes=int(sys.stdin.readline())
lines=int(sys.stdin.readline())
dic=defaultdict(list)
for _ in range(lines):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

def bfs():
    visited=[]
    queue=deque()
    queue.append(1)
    while queue:
        out=queue.popleft()
        if out not in visited:
            visited.append(out)
            for node in dic[out]:
                if node not in visited:
                    queue.append(node)
    return visited
print(len(bfs())-1)

        