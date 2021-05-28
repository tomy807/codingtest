def solution(N, stages):
    answer = []
    stages.sort()
    lenght=len(stages)
    counter={}
    ans=[]
    for i in stages:
        if i not in counter:
            counter[i]=0
        counter[i]+=1
    num=0
    for i in range(1,N+1):
        value=counter.get(i)
        if value:
            ans.append([value/(lenght-num),i])
            num+=value
        else:
            ans.append([0,i])
    ans.sort(key=lambda x:(x[0],-x[1]), reverse=True)
    for i in ans:
        answer.append(i[1])
    return answer