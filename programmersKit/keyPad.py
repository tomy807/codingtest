def solution(numbers, hand):
    pad={1:[0,0],2:[0,1],3:[0,2],
         4:[1,0],5:[1,1],6:[1,2],
         7:[2,0],8:[2,1],9:[2,2],
         '*':[3,0],0:[3,1],'#':[3,2]}
    answer = ''
    leftHand='*'
    rightHand='#'
    for number in numbers:
        print(leftHand)
        if number in [1,4,7]:
            leftHand=number
            answer+='L'
        elif number in [3,6,9]:
            rightHand=number
            answer+='R'
        else:
            leftDistance=abs(pad[number][0]-pad[leftHand][0])+abs(pad[number][1]-pad[leftHand][1])
            rightDistance=abs(pad[number][0]-pad[rightHand][0])+abs(pad[number][1]-pad[rightHand][1])
            if leftDistance<rightDistance:
                leftHand=number
                answer+='L'
            elif leftDistance>rightDistance:
                rightHand=number
                answer+='R'
            else:
                if hand=="right":
                    rightHand=number
                    answer+='R'
                else:
                    leftHand=number
                    answer+='L'
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))