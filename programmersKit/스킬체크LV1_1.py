def solution(N, stages):
    answer = []
    result=[]
    stage_count={}
    for i in range(1,N+2):
        if i in stages:
            stage_count[i]=stages.count(i)
        else:
            stage_count[i]=0
    tmp=len(stages)
    for i in range(1,N+1):
        answer.append((stage_count[i]/tmp,i))
        tmp-=stage_count[i]
    answer.sort(key=lambda x: (-x[0],x[1]))
    for i in answer:
        result.append(i[1])
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))