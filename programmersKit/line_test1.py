def solution(record):
    answer = []
    countS=0
    a=0
    b=0
    tmps=0
    indexS=[]
    new_record=[list(i.split(' ')) for i in record]
    for rec in new_record:
        rec[1]=int(rec[1])
        rec[2]=int(rec[2])
        if rec[0]=='S':
            countS+=rec[2]
            indexS.append(tmps)
        tmps+=1
    for rec in new_record:
        if countS<=0:
            break
        elif rec[0]=='P'and countS>=rec[2]:
            a+=rec[1]*rec[2]
            countS-=rec[2]
        elif rec[0]=='P' and countS<rec[2]:
            a+=rec[1]*countS
            countS=0
    answer.append(a)
    for i in indexS:
        tmp=new_record[i][2]
        while(tmp>0):
            for j in reversed(range(i)):
                if new_record[j][0]=='P' and tmp>=new_record[j][2]:
                    b+=new_record[j][2]*new_record[j][1]
                    tmp-=new_record[j][2]
                    new_record[j][2]=0
                elif new_record[j][0]=='P' and tmp<new_record[j][2]:
                    b+=new_record[j][1]*tmp
                    new_record[j][2]-=tmp
                    tmp=0
                    break
    answer.append(b)
    return answer
print(solution(["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]))