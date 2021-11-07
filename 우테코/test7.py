def solution(grid, clockwise):
    answer = []
    newgrid=[]
    N=len(grid)
    for i in grid:
        newgrid.append(list(i))
    if clockwise:
        for j in range(N-1,-1,-1):
            li=[]
            li.append(newgrid[j][0])
            k=N-j
            for t in range(k,N):
                for l in range(k-1):
                    li.append(newgrid[t+1][l])
                    li.append(newgrid[t+1][l+1])
            answer.append(li)  
    return answer
print(solution(["1","234","56789"],True))