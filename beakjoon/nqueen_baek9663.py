import sys
def search(board,n):
    answer=0
    raw=len(board)
    if n==raw:
        return 1
    for i in range(raw):
        board[n]=i
        if check(board,n):
            answer+=search(board, n+1)
    return answer

def check(board,n):
    for i in range(n):
        if board[i]==board[n] or abs(board[i]-board[n])==n-i:
            return False
    return True

N=int(sys.stdin.readline())
board=[0]*N
print(search(board, 0))