import sys
N=int(input())
arr=[]
for _ in range(N):
    name,a,b,c=sys.stdin.readline().split()
    arr.append([name,int(a),int(b),int(c)])
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0])