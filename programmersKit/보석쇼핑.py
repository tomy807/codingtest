def solution(gems):
    N=len(gems)
    setN=len(set(gems))
    end=0
    tmp=1000000
    tmplist=[]
    tmpSet=0
    result=[0,0]
    for start in range(N):
        if tmplist:
        # tmplist=gems[start:end]
            tmplist.pop(0)
        tmpSet=len(set(tmplist))
        while tmpSet<setN and end<N:
            tmplist.append(gems[end])
            tmpSet=len(set(tmplist))
            end+=1
        if tmpSet==setN:
            if len(tmplist)<tmp:
                tmp=len(tmplist)
                result[0]=start+1
                result[1]=end
    return result
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))