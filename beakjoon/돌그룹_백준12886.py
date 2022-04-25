from collections import deque
from itertools import combinations

A,B,C=map(int, input().split())

def bfs():
    visited=set()
    queue=deque([])
    queue.append((A,B,C))
    visited.add((A,B,C))
    while queue:
        out=queue.popleft()
        if(out[0]==out[1]==out[2]):
            return 1
        totalSum=sum(out)
        for comb in combinations(out, 2):
            X=comb[0]
            Y=comb[1]
            Z=totalSum-X-Y
            if(Y<X):
                X,Y=Y,X
            if (2*X,Y-X,Z) not in visited:
                queue.append((2*X,Y-X,Z))
                visited.add((2*X,Y-X,Z))
    return 0
print(bfs())