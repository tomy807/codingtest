from itertools import combinations
def solution(nums):
    answer = 0
    count=0
    lis=list(combinations(nums,3))
    print(lis)
    for i in lis:
        count+=1
        number=sum(i)
        for j in range(2,number):
            if number % j==0:
                answer+=1
                break
    return count-answer
print(solution([1,2,3,4]))