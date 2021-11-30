import sys
import heapq
inf=10000
T=int(sys.stdin.readline())
for _ in range(T):
    n,m,t=map(int,sys.stdin.readline().split())
    queue=[]
    graph = [[] for _ in range(n+1)]
    distance=[inf]*(n+1)
    s,g,h=map(int,sys.stdin.readline().split())
    for _ in range(m):
        a,b,d=map(int,sys.stdin.readline().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    t1=int(sys.stdin.readline())
    t2=int(sys.stdin.readline())
    heapq.heappush(queue, (0,s))
    distance[s]=0
    while queue:
        nowEdgeDistance,nowEdge=heapq.heappop(queue)
        for nowToNextDistance,nextEdge in graph[nowEdge]:
            nextEdgeDistance=nowEdgeDistance+nowToNextDistance
            
            if nextEdgeDistance<distance[nextEdge]:
                distance[nextEdge]=nextEdgeDistance
                heapq.heappush(queue, (nextEdgeDistance,nextEdge))
    print(distance)