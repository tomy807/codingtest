from itertools import combinations
def solution(numbers):
    answer=list(set(map(lambda x:x[0]+x[1],combinations(numbers,2))))
    answer.sort()
    return answer
print(solution([5,0,2,7]))