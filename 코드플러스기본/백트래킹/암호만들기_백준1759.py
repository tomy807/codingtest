L,C=map(int, input().split())
chars=list(input().split())
chars.sort()
vowels=['a', 'e', 'i', 'o', 'u']
answer=[]
def dfs(depth):
    if depth==L:
        vowelCount=0
        for i in answer:
            if i in vowels:
                vowelCount+=1
        if vowelCount>=1 and depth-vowelCount>=2:
            print(''.join(answer))
            return
        return
    else:
        for i in range(C):
            if depth==0 or (answer[-1]<chars[i]):
                answer.append(chars[i])
                dfs(depth+1)
                answer.pop()
dfs(0)