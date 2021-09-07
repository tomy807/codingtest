def solution(weights, head2head):
    numberOfBoxers=len(weights)
    rankingBoard=[]
    for i in range(numberOfBoxers):
        fightCnt=0
        winCnt=0
        winOverWeightCnt=0
        for j in range(numberOfBoxers):
            if head2head[i][j]!="N":
                fightCnt+=1 
                if head2head[i][j]=="W":
                    winCnt+=1
                    if weights[i]<weights[j]:
                        winOverWeightCnt+=1
        if fightCnt==0:
            fightCnt=1
        rankingBoard.append((winCnt/(fightCnt),winOverWeightCnt,weights[i],i+1))
    rankingBoard.sort(key=lambda x:(-x[0],-x[1],-x[2],x[3]))
    answer=[i[3] for i in rankingBoard]
    return answer

weights=[145,92,86]	
head2head=["NLW","WNL","LWN"]
print(solution(weights, head2head))
