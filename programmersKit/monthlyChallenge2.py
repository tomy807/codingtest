def solution(n, left, right):
    answer=[]
    start=[left//n,left%n]
    end=[right//n,right%n]

    board=[[0 for _ in range(n)] for _ in range(n)]

    for j in range(start[1],n):
            if(start[0]<=j):
                answer.append(j+1)
            else:
                answer.append(start[0]+1)
    
    for i in range(start[0]+1,end[0]):
        for j in range(n):
            if(i<=j):
                answer.append(j+1)
            else:
                answer.append(i+1)
    for j in range(0,end[1]+1):
            if(end[0]<=j):
                answer.append(j+1)
            else:
                answer.append(end[0]+1)
    
    return answer
print(solution(3,2,5))