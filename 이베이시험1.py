def solution(schedule):
    answer = -1
    result=[1,1,1,1]
    newSchedule=[]
    for i in schedule:
        c=[]
        for j in i:
            c.append(j.split(' '))
        newSchedule.append(c)
out=[]
def dfs(newSchedule,depth):
    if depth==5:
        return
    for i in newSchedule[depth]:
        for j in out:
            if (len(i)==4 and len(j)==4):
                if i[0]==j[0] and i[1]:
                    
        out.append(i)
        dfs(newSchedule, depth+1)
        out.pop()
solution(
[["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"],
["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"],
["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"],
["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"],
["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]])