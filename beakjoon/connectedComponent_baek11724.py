import sys
from collections import defaultdict,deque

N,M=map(int,sys.stdin.readline().split())
dic=defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
visited=[]
que=[]
answer=0
que=deque(que)
for i in range(1,N+1):
    if i in visited:
        continue
    answer+=1
    que.append(i)
    while(que): 
        out=que.popleft()
        if out not in visited:
            visited.append(out)
            for connect in dic[out]:
                if connect in visited:
                    continue
                que.append(connect)
print(answer)