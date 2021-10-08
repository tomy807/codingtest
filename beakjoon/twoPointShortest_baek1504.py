import sys
import heapq

N,E=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
INF=0xffffff
queue=[]
for _ in range(E):
        node1,node2,weight=map(int,sys.stdin.readline().split())
        graph[node1].append((node2,weight))
        graph[node2].append((node1,weight))
stop1,stop2=map(int,sys.stdin.readline().split())

def dijstra(start,end):
    heapq.heappush(queue, (0,start))
    distance=[INF]*(N+1)
    distance[start]=0
    while(queue):
        start_to_now_distance,now_edge=heapq.heappop(queue)
        
        if start_to_now_distance>distance[now_edge]:
            continue
        for next_edge,now_to_next_distance in graph[now_edge]:
            start_to_next_distance=start_to_now_distance + now_to_next_distance
            if start_to_next_distance<distance[next_edge]:
                distance[next_edge]=start_to_next_distance
                heapq.heappush(queue, (start_to_next_distance,next_edge))
    return distance[end]

path1=dijstra(1, stop1)+dijstra(stop1, stop2)+dijstra(stop2, N)
path2=dijstra(1, stop2)+dijstra(stop2, stop1)+dijstra(stop1, N)
if path1>=INF and path2>=INF:
    print(-1)
else:
    print(min(path1, path2))
    
