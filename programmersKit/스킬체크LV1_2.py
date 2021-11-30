def solution(n, lost, reserve):
    answer = 0
    dict_cloths={}
    for i in range(1,n+1):
        tmp=1
        if i in lost:
            tmp-=1
        if i in reserve:
            tmp+=1
        dict_cloths[i]=tmp
    for key,value in dict_cloths.items():
        if value==0:
            if key-1>=0 and dict_cloths[key-1]==2:
                dict_cloths[key-1]-=1
                dict_cloths[key]+=1
            elif key+1 <=n and dict_cloths[key+1]==2:
                dict_cloths[key+1]-=1
                dict_cloths[key]+=1
    for i in dict_cloths.values():
        if i>0:
            answer+=1
    return answer
    
print(solution(3, [3], [1]))