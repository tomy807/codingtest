from collections import defaultdict
def solution(nums):
    answer = 0
    sums=0
    lenght=len(nums)
    dicnums=defaultdict(int)
    for item in nums:
        dicnums[item]+=1
    for i in list(dicnums.keys()):
        if dicnums[i]>0:
            sums+=1
    if sums>lenght/2:
        answer=lenght/2
    else:
        answer=sums
    return answer
print(solution([3,3,3,2,2,4]))