def solution(n, left, right):
    answer = []
    lefty,leftx=left//n,left%n
    righty,rightx=right//n,right%n
    
    firstlist=[lefty+1]*(lefty+1)+[j for j in range(lefty+2,n+1)]
    lastlist=[righty+1]*(righty+1)+[j for j in range(righty+2,n+1)]

    if lefty==righty:
        return firstlist[leftx:rightx+1]

    answer.append(firstlist[leftx:])
    for i in range(lefty+2,righty+1):
        answer.append([i]*i+[j for j in range(i+1,n+1)])
    answer.append(lastlist[:rightx+1])
    return sum(answer,[])
print(solution(4,4,7)) 