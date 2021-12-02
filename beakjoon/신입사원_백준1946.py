import sys
from collections import deque
T=int(input())
for _ in range(T):
    N=int(input())
    scores=[0]*(N+1)
    answer=1
    for _ in range(N):
        a,b=map(int,sys.stdin.readline().split(' '))
        scores[a]=b
    queue=deque(scores[1:])
    out=queue.popleft()
    while queue:
        if queue[0]>out:
            queue.popleft()
        else:
            out=queue.popleft()
            answer+=1
    print(answer)