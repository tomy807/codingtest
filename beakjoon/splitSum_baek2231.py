import sys
N=int(sys.stdin.readline())
def solution():
    for i in range(1,N):
        result=i+sum(map(int,list(str(i))))
        if result==N:
            return i
    return 0
print(solution())
