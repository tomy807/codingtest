import sys
def rgb(n):
    for i in range(1,n):
        N[i][0]+=min(N[i-1][1],N[i-1][2])
        N[i][1]+=min(N[i-1][0],N[i-1][2])
        N[i][2]+=min(N[i-1][0],N[i-1][1])
    return N[n-1]
n=int(sys.stdin.readline())
N=[]
for _ in range(n):
    r,g,b=map(int,sys.stdin.readline().split())
    N.append([r,g,b])
print(min(rgb(n)))