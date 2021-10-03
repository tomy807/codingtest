import sys
N=int(sys.stdin.readline())
Tree=[[] for _ in range(N+1)]
parent=[0 for _ in range(N+1)]
que=[1]
visit=[0 for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)
while(que):
    out=que.pop()
    visit[out]=1
    for i in Tree[out]:
        if visit[i]==1:
            continue
        else:
            parent[i]=out
            que.append(i)
for i in range(2,N+1):
    print(parent[i])
