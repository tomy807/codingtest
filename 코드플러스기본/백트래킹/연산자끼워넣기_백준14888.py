import sys
N=int(input())
nums=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
maxInt,minInt=-sys.maxsize -1, sys.maxsize
def dfs(depth,result,add,sub,mul,div):
    global maxInt,minInt
    if depth==N:
        if maxInt<result:
            maxInt=result
        if minInt>result:
            minInt=result
    else:
        if add>0:
            dfs(depth+1,result+nums[depth],add-1,sub,mul,div)
        if sub>0:
            dfs(depth+1, result-nums[depth], add, sub-1, mul, div)
        if mul>0:
            dfs(depth+1, result*nums[depth], add, sub, mul-1, div)
        if div>0:
            dfs(depth+1, int(result/nums[depth]), add, sub, mul, div-1)
dfs(1, nums[0], a, b, c, d)
print(maxInt)
print(minInt)