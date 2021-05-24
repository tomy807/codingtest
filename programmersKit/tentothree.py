def solution(n):
    answer = 0
    three=[]
    cnt=0
    while True:
        if n<3:
            three.append(n)
            break
        three.append(n%3)
        n=n//3
        if n<3:
            three.append(n)
            break
    while three:
        tmp=three.pop()
        answer+=tmp*3**cnt
        cnt+=1
    return answer
print(solution(1))