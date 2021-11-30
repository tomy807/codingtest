def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        li=bin(i|j)[2:]
        tmp=''
        if len(li)!=n:
            tmp+=' '*(n-len(li))
        for j in li:
            if j=='1':
                tmp+='#'
            else:
                tmp+=' '
        answer.append(tmp)
    return answer
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))