import sys
def findSum(timeList):
    tmp=[]
    tmp.append(timeList[0])
    for i in range(1,len(timeList)):
        tmp.append(tmp[i-1]+timeList[i])
    return sum(tmp)


N=int(sys.stdin.readline())
times=list(map(int, sys.stdin.readline().split(' ')))
times.sort()
print(findSum(times))


