def solution(numbers):
    answer = []
    for number in numbers:
        otherNumber=number+1
        if number%2==0:
            answer.append(number+1)
            continue
        else:
            bitNumber=bin(number)
            print(bitNumber)
            while(True):
                
                different=bin(number^otherNumber).count('1')
                if different<=2:
                    answer.append(otherNumber)
                    print(bin(otherNumber))
                    break
                otherNumber+=1
    return answer

print(solution([3,5,7,9,11]))  