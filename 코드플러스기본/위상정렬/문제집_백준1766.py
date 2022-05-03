import heapq
N,M=map(int,input().split())
graph=[set() for _ in range(N+1)]
inDegree=[0 for _ in range(N+1)]
heap=[]
answer=[]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].add(b)
    inDegree[b]+=1
for i in range(1,N+1):
    if inDegree[i]==0:
        heapq.heappush(heap,i)

while heap:
    out=heapq.heappop(heap)
    answer.append(out)
    for i in graph[out]:
        inDegree[i]-=1
        if inDegree[i]==0:
            heapq.heappush(heap,i)
print(answer)