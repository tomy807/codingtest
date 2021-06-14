import sys
import pprint
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
global matrix1
global matrix2
matrix1=[]
matrix2=[[0 for _ in range(x)] for _ in range(y)]
for _ in range(y):
    line=list(map(int,sys.stdin.readline().split()))
    matrix1.append(line)
print(matrix1)
def count():
    global matrix1
    global matrix2
    matrix2=[[0 for _ in range(x)] for _ in range(y)]
    pivot=0
    x0,y0=map(int,sys.stdin.readline().split())
    pivot=matrix1[y0][x0]
    matrix2[y0][x0]=1/pivot
    for i in range(y):
        if i==y0:
            for j in range(x):
                if j==x0:
                    continue
                else:
                    matrix2[i][j]=matrix1[i][j]/pivot
        else:
            for j in range(x):
                if j==x0:
                    matrix2[i][j]=-matrix1[i][j]/pivot
                else:
                    matrix2[i][j]=matrix1[i][j]-(matrix1[y0][j]*matrix1[i][x0])/pivot
    pprint.pprint(matrix2)                
while True:
    print("계속할거면 1 관둘거면 0")
    quit=int(input())
    if quit==1:
        count()
        matrix1=matrix2
    else:
        break                    
