import sys
N=int(sys.stdin.readline())
def solution(N):
    pack3=0
    pack5=0
    temp5=N//5
    for i in range(temp5,-1,-1):
        pack5=i
        pack3=(N-pack5*5)//3
        rest=N-pack5*5-pack3*3
        if rest==0:
            return pack5+pack3
    return -1
print(solution(N))   