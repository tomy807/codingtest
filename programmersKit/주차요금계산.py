from collections import defaultdict
import math
def solution(fees, records):
    inoutTime=defaultdict(list)
    MaxTime=1439
    answer = []
    for record in records:
        splitRecord=record.split()
        time=splitRecord[0]
        timeSplit=time.split(':')
        intTime=int(timeSplit[0])*60+int(timeSplit[1])
        carNum=splitRecord[1]
        inoutTime[carNum].append(intTime)
    k=sorted(inoutTime.items())
    for times in k:
        times=times[1]
        tmp=0
        lenTimes=len(times)
        if lenTimes%2==0:
            for i in range(lenTimes-1,0,-2):
                tmp+=(times[i]-times[i-1])
        else:
            tmp+=MaxTime-times[-1]
            for i in range(lenTimes-2,0,-2):
                tmp+=(times[i]-times[i-1])
        print(tmp)
        if(tmp<=fees[0]):
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil(((tmp-fees[0])/fees[2]))*fees[3])
    return answer

print(solution([180, 5000, 10, 600], 
["05:34 5961 IN",
 "06:00 0000 IN",
 "06:34 0000 OUT",
 "07:59 5961 OUT",
 "07:59 0148 IN",
 "18:59 0000 IN",
 "19:09 0148 OUT",
 "22:59 5961 IN",
 "23:00 5961 OUT"]))