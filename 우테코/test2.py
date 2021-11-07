def solution(log):
    newlog=[]
    answer = ''
    studycount=len(log)//2
    studyTime=[]
    for l in log:
        newlog.append(list(map(int,l.split(':'))))
    for i in range(studycount):
        endTotal=newlog[2*i+1][0]*60+newlog[2*i+1][1]
        startTotal=newlog[2*i][0]*60+newlog[2*i][1]
        total=endTotal-startTotal
        if total<5:
            pass
        elif total>105:
            studyTime.append(105)
        else:
            studyTime.append(total)
    result=sum(studyTime)
    hour=result//60
    minute=result%60
    if hour<10 and minute<10:
        answer='0'+str(hour)+':'+'0'+str(minute)
    elif hour<10 and minute>=10:
        answer='0'+str(hour)+':'+str(minute)
    elif hour>=10 and minute<10:
        answer=str(hour)+':'+'0'+str(minute)
    else:
        answer=str(hour)+':'+str(minute)
    return answer
print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))