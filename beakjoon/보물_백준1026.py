import sys
N=int(sys.stdin.readline())
line=[]
answer=0
for i in range(2):
    line.append(list(map(int,sys.stdin.readline().split(' '))))
    if i==0:
        line[i].sort()
    else:
        line[i].sort(reverse=True)
for i in range(N):
    answer+=line[0][i]*line[1][i]
print(answer)