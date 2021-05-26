import sys
def dp(n):
    for i in range(1,n):
        triangle[i][0]=triangle[i][0]+triangle[i-1][0]
        triangle[i][i]+=triangle[i-1][i-1]
        for j in range(1,i):
            triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    return triangle[n-1]
n=int(sys.stdin.readline())
triangle=[]
for _ in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    triangle.append(line)
print(max(dp(n)))

