def solution(startNumber, endNumber):
    save='000000000'+str(startNumber)
    answer = [save]
    if startNumber<endNumber:
        while(startNumber<endNumber):
            startNumber+=1
            save=save[1:]+str(startNumber)
            answer.append(save)
    else:
        while(startNumber>endNumber):
            startNumber-=1
            save=save[1:]+str(startNumber)
            answer.append(save)
    return answer
print(solution(9, 1))