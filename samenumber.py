def solution(arr):
    out=arr.pop()
    answer = []
    answer.append(out)
    while arr:
        out=arr.pop()
        if answer[-1]==out:
            continue
        else:
            answer.append(out)
    answer.reverse()
    return answer
print(solution([1,1,3,3,0,1,1]))