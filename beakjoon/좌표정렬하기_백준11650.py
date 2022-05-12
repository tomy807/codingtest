import sys
N=int(input())
arr=[]
for _ in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    arr.append(a)
arr.sort(key=lambda x:(x[0],x[1]))
for i in arr:
    print(*i)