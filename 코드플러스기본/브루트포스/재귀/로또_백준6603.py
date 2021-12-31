def dfs(depth):
    global out,visited,K,S
    if depth==6:
        print(*out)
        return
    for i in range(K):
        if len(out)==0 or (not visited[i] and out[-1]< S[i]):
            out.append(S[i])
            visited[i]=True
            dfs(depth+1)
            out.pop()
            visited[i]=False
while(True):
    line=list(map(int, input().split(' ')))
    if line[0]==0:
        break
    else:
        K=line[0]
        S=sorted(line[1:])
        visited=[False]*K
        out=[]
        dfs(0)
        print('')