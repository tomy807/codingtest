import sys
from collections import deque,defaultdict
nodes, line, start=map(int,sys.stdin.readline().split())
dic=defaultdict(list)
for _ in range(line):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
def bfs(start):
    queue=deque()
    queue.append(start)
    visited=[]
    while queue:
        out=queue.popleft()
        if out not in visited:
            visited.append(out)
            print(out, end=' ')
            tmp=sorted(dic[out])
            for value in tmp:
                if value in visited:
                    continue
                else:
                    queue.append(value)
    
def dfs(start):
    stack=[]
    stack.append(start)
    visited=[]
    while stack:
        out=stack.pop()
        if out not in visited:
            visited.append(out)
            print(out, end=' ')
            tmp=sorted(dic[out],reverse=True)
            for value in tmp:
                if value in visited:
                    continue
                else:
                    stack.append(value)
    
dfs(start)
print()
bfs(start)
