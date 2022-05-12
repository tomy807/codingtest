import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    a,b=map(str,sys.stdin.readline().split())
    a=int(a)
    arr.append([a,b])
arr.sort(key=lambda x:x[0])
for i in arr:
    print(*i)