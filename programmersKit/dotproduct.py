def solution(a, b):
    answer = 1234567890
    answer=sum(map(lambda x:x[0]*x[1],zip(a,b)))
    return answer
print(solution([1,2,3,4],[1,2,3,4]))