import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
X=list(map(int,sys.stdin.readline().split()))
A.sort()

def BinarySearch(target):
    low=0
    high=N-1
    while(low<=high):
        mid=int((low+high)/2)
        if A[mid]==target:
            return 1
        elif A[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return 0
def solution():
    for target in X:
        print(BinarySearch(target))
solution()       
