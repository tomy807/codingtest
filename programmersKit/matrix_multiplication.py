def multiple(a,b):
    answer=0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer
def solution(arr1, arr2):
    answer=[[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    new_arr2=list(map(list, zip(*arr2)))
    for i in range(len(arr1)):
        for j in range(len(new_arr2)):
            answer[i][j]=multiple(arr1[i], new_arr2[j])
    return answer
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))