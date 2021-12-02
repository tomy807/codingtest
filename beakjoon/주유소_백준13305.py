from collections import deque
N=int(input())
load=[*map(int,input().split(' '))]
queue=deque(list(map(int,input().split(' ')))[:-1])
answer=0
flag=0
out=queue.popleft()
answer+=out*load[flag]
while queue:
    if out>queue[0]:
        out=queue.popleft()
    else:
        queue.popleft()
    flag+=1
    answer+=out*load[flag]
print(answer)