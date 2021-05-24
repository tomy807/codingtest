import sys 
from collections import deque,defaultdict
answer=[]
def bfs(x,y):
    column, row=len(ground[0]),len(ground)
    if ground[x][y]==1:
        dx=[-1, 1, 0, 0]
        dy=[0, 0, -1, 1]
        queue=deque()
        queue.append((x,y))
        while queue:
            out=queue.popleft()
            for i in range(4):
                nx=out[0]+dx[i]
                ny=out[1]+dy[i]
                if 0<= nx <row and 0<= ny <column and ground[nx][ny]==1:
                    ground[nx][ny]=0
                    queue.append((nx,ny))
        return 1 
    else: 
        return 0
def run_bfs(ground):
    column, row=len(ground[0]),len(ground)
    sum=0
    for i in range(row):
        for j in range(column):
            sum+=bfs(i,j)
    return(sum)

testcase=int(sys.stdin.readline())
for _ in range(testcase):
    column, row, lines=map(int,sys.stdin.readline().split())
    ground=[[0 for _ in range(column)] for _ in range(row)]
    for _ in range(lines):
        j,i=map(int,sys.stdin.readline().split())
        ground[i][j]=1
    answer.append(run_bfs(ground))
for i in answer:
    print(i)



