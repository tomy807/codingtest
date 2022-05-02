def dfs(depth):
    global k,S,answer
    if depth==6:
        for i in answer:
            print(i,end=' ')
        print()
    else:
        for j in range(k):
            if answer[depth-1]<S[j]:
                answer[depth]=S[j]
                dfs(depth+1)


while True:
    global k,S,answer
    line=list(map(int, input().split()))
    k=line[0]
    S=line[1:]
    if k==0:
        break
    answer=[0]*6
    for i in S[0:k-5]:
        answer[0]=i
        dfs(1)
    print()
