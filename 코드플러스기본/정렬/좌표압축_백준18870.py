import sys
N=int(sys.stdin.readline())
X=list(map(int,sys.stdin.readline().split()))
setX = sorted(list(set(X)))
dictX=dict()
for i in range(len(setX)):
    out=setX[i]
    dictX[out]=i
for i in X:
    print(dictX[i])