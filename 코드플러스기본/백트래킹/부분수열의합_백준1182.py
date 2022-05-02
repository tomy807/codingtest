N,S= map(int, input().split())
nums=list(map(int, input().split()))
global answer
answer=0
if answer==S:
    answer-=1
def solution(depth,sums):
    global answer
    if depth==N:
        if sums==S:
            answer+=1
        else:
            return
    else:
        solution(depth+1, sums+nums[depth])
        solution(depth+1, sums)
solution(0, 0)

print(answer)