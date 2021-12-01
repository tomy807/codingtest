import sys

N=int(sys.stdin.readline())
conferences=[]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    conferences.append((a,b))
conferences.sort(key=lambda x:(x[1],x[0]))
last=0
answer=0
for i in conferences:
    if i[0]>=last:
        answer+=1
        last=i[1]
print(answer)