def solution(sortedArray, findValue):
    left=0
    right=len(sortedArray)

    while left<=right:
        middle=(left+right)//2
        if sortedArray[middle]==findValue:
            return middle
        elif sortedArray[middle]>findValue:
            right=middle-1
        else:
            left=middle+1
    return -1
print(solution(	[1, 2, 5, 7, 10, 15, 18, 20], 17))