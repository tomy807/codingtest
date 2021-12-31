N,S=map(int, input().split(' '))
nums=list(map(int, input().split(' ')))
answer=0
def dfs(s,depth):
    global answer
    if depth>=N:
        return
    s+=nums[depth]
    if s==S:
        answer+=1
    dfs(s, depth+1)
    dfs(s-nums[depth], depth+1)
dfs(0,0)
print(answer)