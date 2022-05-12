def solution(s):
    count=[]
    N=len(s)
    # tooth
    # 01234
    for i in range(N-1):
        x0,y0=found(s[i])
        x1,y1=found(s[i+1])
        count.append(abs(x0-x1)+abs(y0-y1))
    answer=sum(count)
    for j in range(2,N):
        for k in range(N-j):
            answer+=sum(count[k:k+j])
    return answer
def found(word):
    keyBoards=["qwertyuio","pasdfghjk","lzxcvbnm"]
    y=0
    for keyBoard in keyBoards:
        x=keyBoard.find(word)
        if x!=-1:
            return x,y
        y+=1