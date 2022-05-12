def solution(grid):
    answer = []
    result=[]
    points=[grid[0][i] for i in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(abs(points[i]-points[j])!=grid[i][j]):
                points[i]=-points[i]
    array=[[i,points[i]] for i in range(len(points))]
    array.sort(key=lambda x: x[1])
    for t in array:
        answer.append(t[0])
    result.append(answer)
    result.append(answer[::-1])
    result.sort()
    return result
print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))