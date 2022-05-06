import sys
N=int(input())
cards=list(map(int, sys.stdin.readline().split()))
M=int(input())
targets=list(map(int, sys.stdin.readline().split()))
answer=[]
cards.sort()

def binarysearch(target):
    left=0
    right=N-1
    while(left<=right):
        mid=(left+right)//2
        if cards[mid]==target:
            return 1
        else:
            if cards[mid]<target:
                left=mid+1
            else:
                right=mid-1
    return 0
for target in targets:
    answer.append(binarysearch(target))
print(*answer)