import sys
from collections import deque
N=int(input())
M=int(input())
bus_dict = {i: [] for i in range(1, N+1)}
distances=[float('inf')]*(N+1)
for _ in range(M):
    s,d,w=map(int,sys.stdin.readline().split())
    bus_dict[s].append([d,w])
start, target = map(int, sys.stdin.readline().split())
queue=deque([(start,0)])
distances[start]=0
while(queue):
    out=queue.popleft()
    now_node,now_distance=out[0],out[1]
    if distances[now_node] <now_distance:
        continue
    else:
        for new_node,new_distance in bus_dict[now_node]:
            distance=now_distance+new_distance
            if distance<distances[new_node]:
                distances[new_node]=distance
                queue.append((new_node,distance))
print(distances[target])