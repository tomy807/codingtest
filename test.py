import heapq
def solution(n, edge):
    answer = 0
    b=dict()
    for i in range(1,n+1):
        b[i]=[]
    for j in edge:
        b[j[0]].append(j[1])
        b[j[1]].append(j[0])
    last_distance=dijkstra(b,n)
    max_distance=max(last_distance)
    for i in last_distance:
        if i==max_distance:
            answer+=1
    return answer

def dijkstra(graph,n):
    distances=[float('inf')]*n
    distances[0]=0
    queue=[]
    heapq.heappush(queue,[distances[0],1])
    print(queue)
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        if distances[current_node-1] <current_distance:
            continue
        for adjacent in graph[current_node]:
            distance=current_distance+1
            
            if distance <distances[adjacent-1]:
                distances[adjacent-1] = distance
                heapq.heappush(queue,[distance,adjacent])
        print(queue)
    return distances
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))