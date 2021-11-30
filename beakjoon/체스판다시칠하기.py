import sys

N,M=map(int,sys.stdin.readline().split())
answer=[]
chessBoard=[]
for _ in range(N):
    chessBoard.append(sys.stdin.readline().rstrip())
for i in range(N-7):
    for j in range(M-7):
        index1=0
        index2=0
        for p in range(i,i+8):
            for q in range(j,j+8):
                if (p+q)%2==0:
                    if chessBoard[p][q]=='B':index1+=1
                    elif chessBoard[p][q]=='W':index2+=1
                else:
                    if chessBoard[p][q]=='W':index1+=1
                    elif chessBoard[p][q]=='B':index2+=1
        answer.append(min(index1,index2))
print(min(answer))