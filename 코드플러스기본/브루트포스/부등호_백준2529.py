import sys
K=int(input())
signs=list(input().split(' '))
out=[]
visited=[False]*10
def maxSign(depth):
    if depth==K:
        return 
    for i in range(9,-1,-1):
        
        out.append(i)
        
        maxSign(depth+1)
