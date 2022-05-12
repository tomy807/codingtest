import sys
from itertools import permutations
N=int(sys.stdin.readline())
AN=list(map(int,sys.stdin.readline().split(' ')))
opercount=list(map(int,sys.stdin.readline().split(' ')))
operation=[]
answer=[]
operation.extend('+'*opercount[0])
operation.extend('-'*opercount[1])
operation.extend('*'*opercount[2])
operation.extend('/'*opercount[3])
combiOperations=list(permutations(operation))
for combiOperation in combiOperations:
    A0=AN[0]
    for i in range(1,N):
        if combiOperation[i-1]=='+':
            A0+=AN[i]
        elif combiOperation[i-1]=='-':
            A0-=AN[i]
        elif combiOperation[i-1]=='*':
            A0*=AN[i] 
        else:
            if A0<0:
                A0=-(-A0//AN[i])
            else:
                A0=A0//AN[i]
    answer.append(A0)
print(max(answer))
print(min(answer))