def solution(time, plans):
    MonStart=13
    MonEnd=18
    FriStart=9.5
    FriEnd=18
    answer=''
    for plan in plans:
        takeTime=0
        place=plan[0]
        if plan[1][-2:]=="AM":
            FriplanStart=int(plan[1][:-2])
        elif plan[1][-2:]=="PM":
            FriplanStart=int(plan[1][:-2])+12
        if plan[2][-2:]=="AM":
            MonplanEnd=int(plan[2][:-2])
        elif plan[2][-2:]=="PM":
            MonplanEnd=int(plan[2][:-2])+12
        if possible(FriplanStart, MonplanEnd)>time:
            continue
        answer=place
    return answer

def possible(FriplanStart,MonplanEnd):
    total=0
    MonStart=13
    MonEnd=18
    FriStart=9.5
    FriEnd=18
    Fri=FriEnd-FriplanStart
    Mon=MonplanEnd-MonStart
    if Fri>=0 and Mon>=0:
        total=Fri+Mon
    elif Fri>=0 and Mon<0:
        total=Fri
    elif Fri<0 and Mon>=0:
        total=Mon
    else:
        total=0
    print(total)
    return total

print(solution(3.5, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]))