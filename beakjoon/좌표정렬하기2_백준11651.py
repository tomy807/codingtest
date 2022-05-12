import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    arr.append(a)
arr.sort(key=lambda x:(x[1],x[0]))
for i in arr:
    print(*i)