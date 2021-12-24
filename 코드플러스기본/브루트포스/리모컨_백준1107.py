N=int(input())
notWorking=int(input())
enableButtons={'0','1','2','3','4','5','6','7','8','9'}-set((map(str,input().split(' '))))
minCnt=abs(100-N)

for num in range(1000001):
    num=str(num)
    for j in range(len(num)):
        if num[j] not in enableButtons:
            break
        elif j==len(num)-1:
            minCnt=min(minCnt, abs(N-int(num))+len(str(num)))
print(minCnt)