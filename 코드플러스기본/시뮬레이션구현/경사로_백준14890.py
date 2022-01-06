N,L=map(int, input().split(' '))
graph=[]
for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

def check(line):
    installed=[False]*N
    for i in range(N-1):
        if line[i]==line[i+1]:
            continue
        if abs(line[i]-line[i+1])>1:
            return False
        if line[i]>line[i+1]:
            tmp=line[i+1]
            for j in range(i+1,i+L+1):
                if j>N-1:
                    return False
                else:
                    if line[j]==tmp and not installed[j]:
                        installed[j]=True
                    else:
                        return False
        else:
            tmp=line[i]
            for j in range(i,i-L,-1):
                if j<0:
                    return False
                else:
                    if line[j]==tmp and not installed[j]:
                        installed[j]=True
                    else:
                        return False   
    return True
answer=0
for line in graph:
    if check(line):
        answer+=1
for i in range(N):
    tmp=[]
    for j in range(N):
        tmp.append(graph[j][i])
    if check(tmp):
        answer+=1
print(answer)