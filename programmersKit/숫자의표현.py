def solution(n):
    if n==1:
        return 1
    answer=0
    left=1
    right=2
    sum=3
    while(right<=n):
        if(sum<n):
            right+=1
            sum+=right
        elif(sum>n):
            sum-=left
            left+=1
        else:
            answer+=1
            sum-=left
            left+=1
    return answer