from itertools import combinations
def solution(line):
    lineCombinations=list(combinations(line, 2))
    coordinates=[]
    for lineCombination in lineCombinations:
        A=lineCombination[0][0]
        B=lineCombination[0][1]
        E=lineCombination[0][2]
        C=lineCombination[1][0]
        D=lineCombination[1][1]
        F=lineCombination[1][2]
        denominator=A*D-B*C
        if denominator!=0:
            x=(B*F-E*D)/denominator
            y= (E*C-A*F)/denominator
            if x-int(x) or y-int(y) : continue
            x,y=int(x),int(y)
            coordinates.append([x,y])
    
    xCoordinates,yCoordinates=list(zip(*coordinates))
    yTopCoordinates=max(yCoordinates)
    yBottomCoordinates=min(yCoordinates)
    xTopCoordinates=max(xCoordinates)
    xBottomCoordinates=min(xCoordinates)
    
    answer = ["."*(xTopCoordinates-xBottomCoordinates+1)]*(yTopCoordinates-yBottomCoordinates+1)
    for coordinate in coordinates:
        answer[yTopCoordinates-coordinate[1]]=answer[yTopCoordinates-coordinate[1]][:coordinate[0]-xBottomCoordinates]+'*'+answer[yTopCoordinates-coordinate[1]][coordinate[0]-xBottomCoordinates+1:]
    return answer
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))