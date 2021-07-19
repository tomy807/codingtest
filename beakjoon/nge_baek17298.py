import sys
from collections import deque
line_length=int(sys.stdin.readline())
# [1,2,3,4]
lis=list(map(int,sys.stdin.readline().split(' ')))  
result=[-1]*line_length
stack=deque()
for i in range(line_length):
    while stack and(stack[-1][0]<lis[i]):
        tmp,idx=stack.pop()
        result[idx]=lis[i]
    stack.append([lis[i],i])

print(*result)
