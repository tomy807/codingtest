def solution(arr):
    answer = []
    count123=[]
    for i in range(1,4):
        count123.append(arr.count(i))
    max123=max(count123)
    for i in range(3):
        answer.append(max123-count123[i])
    return answer
print(solution([1, 2, 3]))