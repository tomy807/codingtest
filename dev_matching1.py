def solution(drum):
    answer = 0
    move={'#':[0,1],'>':[1,0],'<':[-1,0],'*':[0,1]}
    N=len(drum)
    for i in range(N):
        x=i
        y=0
        count=0
        while(y<N):
            tmp=drum[y][x]
            if tmp=='*' and count==1:
                break
            else:
                if tmp=='*':
                    count+=1
                x+=move[tmp][0]
                y+=move[tmp][1]
        if y==N:
                answer+=1  
    return answer


print(solution(["######",">#*###","####*#","#<#>>#",">#*#*<","######"]))