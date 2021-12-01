import sys
N=int(input())
answer=0
weights=[]
for _ in range(N):
    weights.append(int(sys.stdin.readline()))
weights.sort()
for i in range(N):
    answer=max(answer,weights[i]*(N-i))
print(answer)