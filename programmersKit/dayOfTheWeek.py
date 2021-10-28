def solution(a, b):
    MonthlyDays=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    for i in range(0,a-1):
        days+=MonthlyDays[i]
    days=days+b-1
    day=(days)%7
    if day==0:
        return "FRI"
    elif day==1:
        return "SAT"
    elif day==2:
        return "SUN"
    elif day==3:
        return "MON"
    elif day==4:
        return "TUE"
    elif day==5:
        return "WED"
    else:
        return "THU"   

print(solution(1,31))


