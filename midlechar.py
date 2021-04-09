def solution(s):
    lens=len(s)
    answer = ''
    if lens<=2:
        return s
    else:
        if lens%2==0:
            answer=s[lens//2-1:lens//2+1]
        else:
            answer=s[lens//2]
    return answer
print(solution("qwer"))