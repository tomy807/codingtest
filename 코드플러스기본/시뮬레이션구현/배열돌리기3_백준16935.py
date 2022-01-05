import sys
N,M,R=map(int, input().split(' '))
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().split(' '))))
operations=list(map(int,sys.stdin.readline().split(' ')))
def operation1():
    global matrix
    matrix.reverse()
def operation2():
    global matrix
    for i in range(N):
        matrix[i].reverse()
# 시계 90도
def operation3():
    global matrix
    new_matrix=[[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_matrix[i][j]=matrix[N-j-1][i]
    matrix=new_matrix
# 반시계 90도
def operation4():
    global matrix
    new_matrix=[[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_matrix[i][j]=matrix[j][M-i-1]
    matrix=new_matrix

def operation5():
    global matrix
    m=M
    n=N
    new_matrix = [[0] * m for _ in range(n)]
    for i in range(n // 2):    
        for j in range(m // 2):
            new_matrix[i][j + m // 2] = matrix[i][j]
    for i in range(n // 2):    
        for j in range(m // 2, m):
            new_matrix[i + n // 2][j] = matrix[i][j]
    for i in range(n // 2, n):    
        for j in range(m // 2, m):
            new_matrix[i][j - m // 2] = matrix[i][j]
    for i in range(n // 2, n):    
        for j in range(m // 2):
            new_matrix[i - n // 2][j] = matrix[i][j]
    matrix=new_matrix

def operation6():
    global matrix
    m=M
    n=N
    new_matrix = [[0] * m for _ in range(n)]
    for i in range(n // 2):    
        for j in range(m // 2):
            new_matrix[i + n // 2][j] = matrix[i][j]
    for i in range(n // 2, n):    
        for j in range(m // 2):
            new_matrix[i][j + m // 2] = matrix[i][j]
    for i in range(n // 2, n):    
        for j in range(m // 2, m):
            new_matrix[i - n // 2][j] = matrix[i][j]
    for i in range(n // 2):    
        for j in range(m // 2, m):
            new_matrix[i][j - m // 2] = matrix[i][j]
    matrix=new_matrix
for operation in operations:
    if operation == 1:
        operation1()
    elif operation == 2:
        operation2()
    elif operation == 3:
        operation3()
        N,M=M,N
    elif operation == 4:
        operation4()
        N,M=M,N
    elif operation == 5:
        operation5()
    else:
        operation6()
for i in matrix:
    print(*i)