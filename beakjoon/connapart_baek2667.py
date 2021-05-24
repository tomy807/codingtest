import sys
from collections import deque,defaultdict
data=[]
visited=[]
answerli=[]
lines=int(sys.stdin.readline())
for _ in range(lines):
    line=list(map(int,list(sys.stdin.readline().strip())))
    data.append(line)
def bfs(x,y):
    cnt=0
    if [x,y] in visited or data[x][y]==0:
        return -1
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    queue=deque()
    queue.append([x,y])
    while queue:
        out=queue.popleft()
        if out not in visited:
            visited.append(out)
            cnt+=1
            for i in range(4):
                nx=out[0]+dx[i]
                ny=out[1]+dy[i]
                if(nx<0 or nx>=lines or ny<0 or ny>=lines) : continue
                if [nx,ny] in visited or data[nx][ny]==0:
                    continue
                else:
                    queue.append([nx,ny])
    return cnt


for i in range(lines):
    for j in range(lines):
        answer=bfs(i,j)
        if answer==-1:
            continue
        else:
            answerli.append(answer)
print(len(answerli))
answerli.sort()
for k in answerli:
    print(k)