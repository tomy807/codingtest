def solution(n):
    graph=[[0 for _ in range(i)] for i in range(1,n+1)]
    x=0
    y=-1
    count=1
    for i in range(n):
        for j in range(n-i):
            if i%3==0:
                y+=1
                graph[y][x]=count
            elif i%3==1:
                x+=1
                graph[y][x]=count
            else:
                y-=1
                x-=1
                graph[y][x]=count
            count+=1
    return sum(graph,[])
print(solution(5))