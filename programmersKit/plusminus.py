def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i]=-absolutes[i]
    answer=sum(absolutes)
    return answer
print(solution([4,7,12],[True,False,True]))