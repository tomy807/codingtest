from collections import deque
N,K=map(int,input().split(' '))
dist=[-1]*100001

def bfs(N):
    queue=deque([N])
    dist[N]=0
    while queue:
        out=queue.popleft()
        if out==K:
            return
        for nextX in (out-1,out+1,out*2):
            if 0<=nextX<100001 and dist[nextX]==-1:    
                if nextX==out*2:
                    dist[nextX]=dist[out]
                    queue.appendleft(nextX)
                else:
                    dist[nextX]=dist[out]+1
                    queue.append(nextX)

bfs(N)
print(dist[K])