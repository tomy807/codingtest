import sys
N = int(input())
requests = list(map(int, sys.stdin.readline().split()))
budget = int(input())
requests.sort()

def solution():
    left = 1
    right = requests[-1]
    while(left <= right):
        mid = (left+right)//2
        totalSum=0
        for request in requests:
            if request<=mid:
                totalSum+=request
            else:
                totalSum+=mid
        if totalSum>budget:
            right=mid-1
        else:
            left=mid+1
    return right
print(solution())