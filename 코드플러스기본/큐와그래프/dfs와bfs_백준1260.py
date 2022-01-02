import sys
from collections import defaultdict,deque
N,M,V=map(int, sys.stdin.readline().split(' '))
graph=defaultdict(list)
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited.append(node)
    print(node,end=' ')
    for i in sorted(graph[node]):
        if i in visited:
            continue
        else:
            dfs(i)
def bfs(V):
    queue=deque([V])
    visited=[V]
    while queue:
        out=queue.popleft()
        print(out,end=' ')
        for i in sorted(graph[out]):
            if i not in visited:
                queue.append(i)
                visited.append(i)
visited=[]      
dfs(V)
print()
bfs(V)