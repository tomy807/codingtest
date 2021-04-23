def solution(d,budget):
    d.sort()
    answer=0
    sum=0
    for i in d:
        sum+=i
        if sum>=budget:
            return answer
        answer+=1
    return answer
print(solution([2,2,3,3],10))