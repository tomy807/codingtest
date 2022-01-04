from collections import deque
N,K=map(int,input().split(' '))
dist=[0]*100001
move=[0]*100001
answer=[]
def bfs(start):
    global answer1,answer2
    visited=[]
    queue=deque([])
    queue.append(start)
    while(queue):
        outX=queue.popleft()
        if outX==K:
            answer.append(K)
            tmp=move[K]
            for _ in range(dist[K]):
                answer.append(tmp)
                tmp=move[tmp]             
            return
        for i in (outX+1,outX-1,outX*2):
            if 0<=i<100001 and dist[i]==0:
                queue.append(i)
                dist[i]=dist[outX]+1
                move[i]=outX
bfs(N)
print(dist[K])
print(' '.join(map(str, answer[::-1])))