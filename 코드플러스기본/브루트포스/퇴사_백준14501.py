N=int(input())
programs=[]
for i in range(N):
    programs.append(list(map(int, input().split(' '))))
answer=0
def dfs(depth,sumP):
    global answer
    if depth==N:
        if answer<sumP:
            answer=sumP
        return
    elif depth>N:
        return
    else:
        dfs(depth+programs[depth][0],sumP+programs[depth][1])
        dfs(depth+1,sumP)
dfs(0, 0)
print(answer)