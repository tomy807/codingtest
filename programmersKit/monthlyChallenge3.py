def solution(n, m, x, y, queries):
    answer = -1
    board=[[0 for _ in range(m)] for _ in range(n)]
    S0=[0,-1]
    N1=[0,1]
    W2=[-1,0]
    E3=[1,0]
    # for i in range(n):
        # for j in range(m):
    x=0
    y=0
    for querie in queries:
        if querie[0]==0:
            y-=1*querie[1]
        if querie[0]==1:
            y+=1*querie[1]
        if querie[0]==2:
            x-=1*querie[1]
        if querie[0]==3:
            y+=1*querie[1]
    return answer

def outRange(x,y):
    if 0<=x<=m and 0<=y<=n:
        return True
    else:
        return False
        