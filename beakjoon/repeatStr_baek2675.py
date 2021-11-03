import sys
T=int(sys.stdin.readline())
for _ in range(T):
    answer=''
    R,S=sys.stdin.readline().split(' ')
    R=int(R)
    S=list(S.rstrip())
    for s in S:
        answer+=s*R
    print(answer)