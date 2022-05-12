N=int(input())
arr=[0]*(N)
answer=0
def dfs(x):
    global answer
    if x==N:
        answer+=1
    else:
        for j in range(N):
            arr[x]=j
            if promising(x):
                dfs(x+1)

def promising(x):
    for i in range(x):
        if (arr[i]==arr[x]) or (abs(x-i)==abs(arr[i]-arr[x])):
            return False
    return True
dfs(0)
print(answer)