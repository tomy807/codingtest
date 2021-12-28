import sys
N=int(input())
board=[]
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split(' '))))
visited=[0 for _ in range(N)]
answer=100000
def rec(depth,idx):
    global answer
    if depth==N//2:
        teamA,teamB=0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    teamA+=board[i][j]
                elif not visited[i] and not visited[j]:
                    teamB+=board[i][j]
        answer=min(answer,abs(teamA-teamB))
        if answer==0:
            print(answer)
            exit()
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i]=1
            rec(depth+1,idx+1)
            visited[i]=0
rec(0, 0)
print(answer)