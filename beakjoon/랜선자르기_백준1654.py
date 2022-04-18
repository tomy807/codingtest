import sys
K,N=map(int, sys.stdin.readline().split())
lines=[]
for _ in range(K):
    lines.append(int(sys.stdin.readline()))
lines.sort()
left=1
right=lines[K-1]
while left<=right:
    sliceCnt=0
    middle=(left+right)//2
    for line in lines:
        sliceCnt+=(line//middle)
    if sliceCnt<N:
        right=middle-1
    else:
        left=middle+1
print(right)