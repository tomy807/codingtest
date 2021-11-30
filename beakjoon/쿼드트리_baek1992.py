import sys
N=int(sys.stdin.readline())
graph=[]
for _ in range(N):
    graph.append(list(map(int,str()(sys.stdin.readline()))))
global answer
answer=''
def rec(a,b,N):
    main=graph[a][b]
    for i in range(a,a+N):
        for j in range(b,b+N):
            if main!=graph[i][j]:
                nn=N//2
                rec(a, b, nn)
                rec(a+nn, b, nn)
                rec(a, b+nn, nn)
                rec(a+nn, b+nn, nn)

