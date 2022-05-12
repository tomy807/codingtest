import sys
H,W,X,Y=map(int, input().split(' '))
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(H+X)]
answer=[[0 for _ in range(W)] for _ in range(H)]
check=[[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i+X<H and j+Y<W:
            check[i+X][j+Y]+=1
        check[i][j]+=1
for i in range(H):
    for j in range(W):
        if check[i][j]==2:
            answer[i][j]=arr[i][j]-arr[i-X][j-Y]
        elif check[i][j]==1:
            answer[i][j]=arr[i][j]
for line in answer:
    print(*line)