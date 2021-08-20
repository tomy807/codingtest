import sys
import heapq

V,E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
INF=100000000
distance = [INF]*(V+1)
queue=[]

for _ in range(E):
    s,e,weight = map(int,sys.stdin.readline().split())
    graph[s].append((e,weight))

def dijstra(start):
    heapq.heappush(queue, (0,start))
    distance[start]=0
    
    while(queue):
        start_to_now_distance,now_edge=heapq.heappop(queue)
        if start_to_now_distance>distance[now_edge]:
            continue
        for next_edge,now_to_next_distance in graph[now_edge]:
            start_to_next_distance= start_to_now_distance + now_to_next_distance
            
            if start_to_next_distance<distance[next_edge]:
                distance[next_edge]=start_to_next_distance
                heapq.heappush(queue, (start_to_next_distance,next_edge))

dijstra(start)
for i in range(1,V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])