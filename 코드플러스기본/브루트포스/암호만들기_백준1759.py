L,C=map(int,input().split(' '))
alphabets=list(input().split(' '))
alphabets.sort()
visited=[False for _ in range(C)]
vowels={'a', 'e', 'i', 'o', 'u'}
out=[]
def dfs(depth):
    if depth==L:
        setOut=set(out)
        if len(setOut&vowels)>=1 and len(setOut-vowels)>=2:
            print(''.join(out))
            return     
        return       
    else:
        for i in range(C):
            if depth==0 or (not visited[i] and out[-1]<alphabets[i]):
                visited[i]=True
                out.append(alphabets[i])
                dfs(depth+1)
                out.pop()
                visited[i]=False
dfs(0)