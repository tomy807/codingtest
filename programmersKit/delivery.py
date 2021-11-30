import heapq

def solution(N, road, K):
    answer = 0
    inf=10000
    distance=[inf]*(N+1)
    graph=[[] for _ in range(N+1)]
    for street in road:
        e1,e2,w=street
        graph[e1].append((e2,w))
        graph[e2].append((e1,w))
    dijstra(1,distance,graph) 
    for i in distance:
        if i<=K:
            answer+=1
    return answer

def dijstra(start,distance,graph):
    queue=[]
    heapq.heappush(queue, (0,start))
    distance[start]=0
    
    while(queue):
        start_to_now_distance,now_edge=heapq.heappop(queue)
        
        for next_edge,now_to_next_distance in graph[now_edge]:
            start_to_next_distance= start_to_now_distance + now_to_next_distance
            
            if start_to_next_distance<distance[next_edge]:
                distance[next_edge]=start_to_next_distance
                heapq.heappush(queue, (start_to_next_distance,next_edge))

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))