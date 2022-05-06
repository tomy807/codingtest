from collections import deque
n=int(input())
Tree=[[] for _ in range(n+1)]
global distances,visited
distances=[0]*(n+1)
visited=[0]*(n+1)
for _ in range(n-1):
    a,b,c=map(int, input().split())
    Tree[a].append([b,c])
    Tree[b].append([a,c])

def findMax(start):
    global distances,visited
    visited[start]=1
    queue=deque([(start,0)])
    while queue:
        node,distance=queue.popleft()
        for nextNode in Tree[node]:
            nodeNum=nextNode[0]
            nextdistance=nextNode[1]
            if visited[nodeNum]==0:
                queue.append((nodeNum,distance+nextdistance))
                visited[nodeNum]=1
                distances[nodeNum] = distance+nextdistance
    return distances.index(max(distances))
  
one=findMax(1)
distances = [0]*(n+1)
visited = [0]*(n+1)
two=findMax(one)
print(distances[two])
