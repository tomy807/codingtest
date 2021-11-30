def solution(leave, day, holidays):
    answer = -1
    firstDay=1
    if day=="MON":
        sat=firstDay+5
        sun=firstDay+6
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="TUE":
        sat=firstDay+4
        sun=firstDay+5
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="WED":
        sat=firstDay+3
        sun=firstDay+4
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="THU":
        sat=firstDay+2
        sun=firstDay+3
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="FRI":
        sat=firstDay+1
        sun=firstDay+2
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="SAT":
        sat=firstDay
        sun=firstDay+1
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7
    if day=="SUN":
        sat=firstDay+6
        sun=firstDay
        while sat<=30:
            holidays.append(sat)
            sat+=7
        while sun<=30:
            holidays.append(sun)
            sun+=7      
    holidays=list(set(holidays))
    holidays.sort()
    sides=[]
    result=[]
    for i in range(len(holidays)-1):
        sides.append(holidays[i+1]-holidays[i]-1)
    print(holidays)
    print(sides)
    for startHoliday  in range(len(holidays)):
        cnt=1
        for i  in range(startHoliday,len(holidays)):
            if holidays-nextDay<0:
                result.append(cnt)
                break
            cnt+=sides[nextDay]+2
            leave-=sides[nextDay]
    answer=max(result)         
    return answer

print(solution(4,	"FRI"	,[6, 21, 23, 27, 28]))
