import sys
N=int(input())
board=[]
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
sameColorCnt=0

def check(board):
    global sameColorCnt
    for line in board:
        cnt=1
        for j in range(1,N):
            if line[j]==line[j-1]:
                cnt+=1
            else:
                if sameColorCnt<cnt:
                    sameColorCnt=cnt
                cnt=1
        if sameColorCnt<cnt:
            sameColorCnt=cnt
    
    if sameColorCnt==N:
        return
    for j in range(N):
        cntY=1
        for i in range(1,N):
            if board[j][i]==board[j-1][i]:
                cntY+=1
            else:
                if sameColorCnt<cntY:
                    sameColorCnt=cntY
                cntY=1
        if sameColorCnt<cntY:
            sameColorCnt=cntY

for i in range(N):
    for j in range(1,N):
        board[i][j],board[i][j-1]=board[i][j-1],board[i][j]
        check(board)
        board[i][j],board[i][j-1]=board[i][j-1],board[i][j]
for i in range(N):
    for j in range(1,N):
        board[j][i],board[j-1][i]=board[j-1][i],board[j][i]
        check(board)
        board[j][i],board[j-1][i]=board[j-1][i],board[j][i]
print(sameColorCnt)